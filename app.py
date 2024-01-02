from typing import List

import peewee
import pypika
import sqlalchemy as sa
from fastapi import Depends, FastAPI, Form
from fastapi_asyncpg import configure_asyncpg
from piccolo import columns as picols
from piccolo.table import Table as PiccoloTable
from playhouse.pool import PooledPostgresqlExtDatabase
from pydantic import BaseModel
from pypika.dialects import PostgreSQLQuery as Query
from sqla_fancy_core import TableFactory
from sqlalchemy.ext.asyncio import create_async_engine

import piccolo_conf

# Peewee -------------------------------------------------------------------------------
peewee_state_default = {"closed": None, "conn": None, "ctx": None, "transactions": None}
peeweedb = PooledPostgresqlExtDatabase(
    "postgres",
    user="dev",
    password="dev",
    host="localhost",
    port=5432,
    max_connections=20,
)
peewee_no_pool_db = peewee.PostgresqlDatabase(
    "postgres", user="dev", password="dev", host="localhost", port=5432
)


class TaskPeewee(peewee.Model):
    id = peewee.AutoField(primary_key=True)
    name = peewee.CharField()
    completed = peewee.BooleanField()

    class Meta:
        database = peeweedb
        table_name = "task"


def peewee_transaction():
    with peeweedb.atomic():
        yield


# Sqlalchemy ---------------------------------------------------------------------------

tf = TableFactory()
sqla_psycopg2_engine = sa.create_engine(
    "postgresql+psycopg2://dev:dev@localhost/postgres", pool_size=20, max_overflow=0
)


sqla_asyncpg_engine = create_async_engine(
    "postgresql+asyncpg://dev:dev@localhost/postgres", pool_size=20, max_overflow=0
)


async def sqla_asyncpg_session():
    async with sqla_asyncpg_engine.begin() as session:
        yield session


def sqla_psycopg2_session():
    with sqla_psycopg2_engine.begin() as session:
        yield session


class TaskSqla:
    id = tf.auto_id()
    name = tf.string("name")
    completed = tf.boolean("completed")

    Table = tf("task")


# Piccolo ------------------------------------------------------------------------------

piccolodb = piccolo_conf.DB


async def piccolo_transaction():
    async with piccolodb.transaction():
        yield


class TaskPiccolo(PiccoloTable, tablename="task"):
    id = picols.Serial(primary_key=True)
    name = picols.Varchar()
    completed = picols.Boolean()


# Asyncpg ------------------------------------------------------------------------------


async def phony(_):
    pass


app = FastAPI()
asyncpgdb = configure_asyncpg(
    app,
    "postgresql://dev:dev@localhost/postgres",
    max_size=20,
    init_db=phony,
)

# Pypika -------------------------------------------------------------------------------


class TaskPypika:
    Table = pypika.Table("task")
    id: pypika.Field = Table.field("id")
    name: pypika.Field = Table.field("name")
    completed: pypika.Field = Table.field("completed")


# --------------------------------------------------------------------------------------


class TaskDTO(BaseModel):
    id: int
    name: str
    completed: bool


@app.on_event("startup")
async def startup():
    peeweedb.create_tables([TaskPeewee])
    await piccolodb.start_connection_pool(max_size=20)


@app.get("/asyncpg", response_model=List[TaskDTO])
async def list_asyncpg(db=Depends(asyncpgdb.atomic)):
    result = await db.fetch("SELECT * FROM task")
    return [dict(row) for row in result]


@app.get("/asyncpg/{id}", response_model=TaskDTO)
async def get_asyncpg(id: int, db=Depends(asyncpgdb.atomic)):
    result = await db.fetch("SELECT * FROM task WHERE id = $1", id)
    return dict(result[0])


@app.get("/pypika-asyncpg", response_model=List[TaskDTO])
async def list_pypika_asyncpg(db=Depends(asyncpgdb.atomic)):
    q = Query.from_(TaskPypika.Table).select("*")
    result = await db.fetch(str(q))
    return [dict(row) for row in result]


@app.get("/pypika-asyncpg/{id}", response_model=TaskDTO)
async def get_pypika_asyncpg(id: int, db=Depends(asyncpgdb.atomic)):
    q = Query.from_(TaskPypika.Table).select("*").where(TaskPypika.id == id)
    result = await db.fetch(str(q))
    return dict(result[0])


@app.get("/sqla-asyncpg", response_model=List[TaskDTO])
async def list_sqla_asyncpg(session=Depends(sqla_asyncpg_session)):
    result = await session.execute(sa.select(TaskSqla.Table))
    return list(result.mappings())


@app.get("/sqla-asyncpg/{id}", response_model=TaskDTO)
async def get_sqla_asyncpg(id: int, session=Depends(sqla_asyncpg_session)):
    result = await session.execute(sa.select(TaskSqla.Table).where(TaskSqla.id == id))
    return next(result.mappings())


@app.get("/sqla-psycopg2", response_model=List[TaskDTO])
def list_sqla_psycopg2(session=Depends(sqla_psycopg2_session)):
    result = session.execute(sa.select(TaskSqla.Table))
    return list(result.mappings())


@app.get("/sqla-psycopg2/{id}", response_model=TaskDTO)
def get_sqla_psycopg2(session=Depends(sqla_psycopg2_session)):
    result = session.execute(sa.select(TaskSqla.Table).where(TaskSqla.id == 1))
    return next(result.mappings())


@app.get("/peewee", response_model=List[TaskDTO])
def list_peewee(_=Depends(peewee_transaction)):
    result = TaskPeewee.select().dicts()
    return result


@app.get("/peewee/{id}", response_model=TaskDTO)
def get_peewee(id: int, _=Depends(peewee_transaction)):
    with peeweedb.atomic():
        result = TaskPeewee.select().where(TaskPeewee.id == id).dicts()
        return result[0]


@app.get("/piccolo", response_model=List[TaskDTO])
async def list_piccolo(_=Depends(piccolo_transaction)):
    result = await TaskPiccolo.select().run()
    return result


@app.get("/piccolo/{id}", response_model=TaskDTO)
async def get_piccolo(id: int, _=Depends(piccolo_transaction)):
    result = await TaskPiccolo.select().where(TaskPiccolo.id == id).first().run()
    return result


@app.get("/peewee-no-pool", response_model=List[TaskDTO])
def list_peewee_no_pool(_=Depends(peewee_transaction)):
    result = TaskPeewee.select().dicts()
    return result


@app.get("/peewee-no-pool/{id}", response_model=TaskDTO)
def get_peewee_no_pool(id: int, _=Depends(peewee_transaction)):
    result = TaskPeewee.select().where(TaskPeewee.id == id).dicts()
    return result[0]


# Test atomicity -----------------------------------------------------------------------


@app.post("/pypika-asyncpg", response_model=int)
async def create_pypika_asyncpg(
    name: str = Form(...), db=Depends(asyncpgdb.atomic)
) -> int:
    q = (
        Query.into(TaskPypika.Table)
        .columns(TaskPypika.name, TaskPypika.completed)
        .insert(name, True)
        .returning(TaskPypika.id)
    )

    result = await db.fetch(str(q))

    # assert False

    q = (
        Query.into(TaskPypika.Table)
        .columns(TaskPypika.name, TaskPypika.completed)
        .insert(str(result[0][TaskPypika.id.name]), True)
        .returning(TaskPypika.id)
    )

    result = await db.fetch(str(q))
    return result[0][TaskPypika.id.name]


@app.post("/sqla-asyncpg", response_model=int)
async def create_sqla_asyncpg(
    name: str = Form(...), session=Depends(sqla_asyncpg_session)
) -> int:
    result = await session.execute(
        sa.insert(TaskSqla.Table)
        .values({TaskSqla.name: name, TaskSqla.completed: True})
        .returning(TaskSqla.id)
    )

    # assert False

    result = await session.execute(
        sa.insert(TaskSqla.Table)
        .values({TaskSqla.name: str(result.scalar_one()), TaskSqla.completed: True})
        .returning(TaskSqla.id)
    )
    return result.scalar_one()


@app.post("/peewee", response_model=int)
def create_peewee(name: str = Form(...), _=Depends(peewee_transaction)) -> int:
    result = TaskPeewee.insert(name=name, completed=False).execute()

    # assert False

    result = TaskPeewee.insert(name=str(result), completed=False).execute()
    return result


@app.post("/piccolo", response_model=int)
async def create_piccolo(name: str = Form(...), _=Depends(piccolo_transaction)) -> int:
    result = (
        await TaskPiccolo.insert(TaskPiccolo(name=name, completed=False))
        .returning(TaskPiccolo.id)
        .run()
    )

    # assert False

    result = (
        await TaskPiccolo.insert(
            TaskPiccolo(name=str(result[0][TaskPiccolo.id]), completed=False)
        )
        .returning(TaskPiccolo.id)
        .run()
    )
    return result[0][TaskPiccolo.id]
