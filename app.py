from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import List

import aiopg
import peewee
import pgmini
import pypika
import sqlalchemy as sa
from fastapi import Depends, FastAPI, Form
from fastapi.responses import ORJSONResponse
from fastapi_asyncpg import configure_asyncpg
from piccolo import columns as picols
from piccolo.table import Table as PiccoloTable
from playhouse.pool import PooledPostgresqlExtDatabase
from psycopg2.pool import ThreadedConnectionPool
from pydantic import BaseModel
from pypika.dialects import PostgreSQLQuery as Query
from sqla_fancy_core import TableFactory
from sqlalchemy.ext.asyncio import create_async_engine

import piccolo_conf

MAX_CONN = 20


# Peewee -------------------------------------------------------------------------------
peeweedb = PooledPostgresqlExtDatabase(
    "postgres",
    user="dev",
    password="dev",
    host="localhost",
    port=5432,
    max_connections=MAX_CONN,
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


class TaskPeeweeNoPool(peewee.Model):
    id = peewee.AutoField(primary_key=True)
    name = peewee.CharField()
    completed = peewee.BooleanField()

    class Meta:
        database = peewee_no_pool_db
        table_name = "task"


def peewee_transaction():
    with peeweedb.atomic():
        yield


def peewee_no_pool_transaction():
    with peewee_no_pool_db.atomic():
        yield


# Sqlalchemy ---------------------------------------------------------------------------

tf = TableFactory()
sqla_psycopg2_engine = sa.create_engine(
    "postgresql+psycopg2://dev:dev@localhost/postgres",
    pool_size=MAX_CONN,
    max_overflow=0,
)


sqla_asyncpg_engine = create_async_engine(
    "postgresql+asyncpg://dev:dev@localhost/postgres",
    pool_size=MAX_CONN,
    max_overflow=0,
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


app = FastAPI(default_response_class=ORJSONResponse)
asyncpgdb = configure_asyncpg(
    app,
    "postgresql://dev:dev@localhost/postgres",
    max_size=MAX_CONN,
    init_db=phony,
)


@app.get("/no-transaction", response_model=list[bool])
async def list_no_trancsction():
    return [True]


@app.get("/no-transaction/{id}", response_model=bool)
async def get_no_trancsction():
    return True


# Pypika -------------------------------------------------------------------------------


class TaskPypika:
    Table = pypika.Table("task")
    id: pypika.Field = Table.field("id")
    name: pypika.Field = Table.field("name")
    completed: pypika.Field = Table.field("completed")


psycopg2_pool = ThreadedConnectionPool(
    1, 20, user="dev", password="dev", host="localhost", port=5432, database="postgres"
)


def psycopg2_transaction():
    conn = psycopg2_pool.getconn()
    cursor = conn.cursor()
    try:
        yield cursor
        conn.commit()
    except:
        conn.rollback()
        raise
    finally:
        psycopg2_pool.putconn(conn)


async def aiopg_transaction():
    pool: aiopg.Pool = app.state.aiopgpool
    async with pool.acquire() as conn:
        async with conn.cursor() as cursor:
            async with cursor.begin():
                yield cursor


# Pgmini -------------------------------------------------------------------------------


class TaskPgmini:
    Table = pgmini.Table("task")
    id = Table.id
    name = Table.name
    completed = Table.completed


# --------------------------------------------------------------------------------------


class TaskDTO(BaseModel):
    id: int
    name: str
    completed: bool


@app.on_event("startup")
async def startup():
    peeweedb.create_tables([TaskPeewee])
    await piccolodb.start_connection_pool(max_size=MAX_CONN)
    app.state.aiopgpool = await aiopg.Pool.from_pool_fill(
        dsn="postgresql://dev:dev@localhost/postgres",
        minsize=1,
        maxsize=MAX_CONN,
        timeout=60,
        enable_json=True,
        enable_hstore=True,
        enable_uuid=True,
        echo=False,
        on_connect=None,
        pool_recycle=-1.0,
    )


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
    q = (
        Query.from_(TaskPypika.Table)
        .select("*")
        .where(TaskPypika.id == pypika.Parameter("$1"))
    )
    result = await db.fetch(str(q), id)
    return dict(result[0])


@app.get("/pgmini-asyncpg", response_model=List[TaskDTO])
async def list_pgmini_asyncpg(db=Depends(asyncpgdb.atomic)):
    sql = pgmini.Select(TaskPgmini.Table.STAR).From(TaskPgmini.Table)
    q, values = pgmini.build(sql, driver="asyncpg")

    result = await db.fetch(q, *values)
    return [dict(row) for row in result]


@app.get("/pgmini-asyncpg/{id}", response_model=TaskDTO)
async def get_pgmini_asyncpg(id: int, db=Depends(asyncpgdb.atomic)):
    sql = (
        pgmini.Select(TaskPgmini.Table.STAR)
        .From(TaskPgmini.Table)
        .Where(TaskPgmini.Table.id == id)
    )
    q, values = pgmini.build(sql, driver="asyncpg")
    result = await db.fetch(str(q), *values)
    return dict(result[0])


@app.get("/pgmini-aiopg", response_model=List[TaskDTO])
async def list_pgmini_aiopg(cursor: aiopg.Cursor = Depends(aiopg_transaction)):
    sql = pgmini.Select(TaskPgmini.id, TaskPgmini.name, TaskPgmini.completed).From(
        TaskPgmini.Table
    )
    q, values = pgmini.build(sql, driver="psycopg")

    await cursor.execute(q, values)
    result = await cursor.fetchall()
    return [
        dict(id=id, name=name, completed=completed) for id, name, completed in result
    ]


@app.get("/pgmini-aiopg/{id}", response_model=TaskDTO)
async def get_pgmini_aiopg(id: int, cursor: aiopg.Cursor = Depends(aiopg_transaction)):
    sql = (
        pgmini.Select(TaskPgmini.id, TaskPgmini.name, TaskPgmini.completed)
        .From(TaskPgmini.Table)
        .Where(TaskPgmini.Table.id == id)
    )
    q, values = pgmini.build(sql, driver="psycopg")
    await cursor.execute(q, values)
    id, name, completed = await cursor.fetchone()
    return dict(id=id, name=name, completed=completed)


@app.get("/pgmini-psycopg2", response_model=List[TaskDTO])
def list_pgmini_psycopg2(cursor=Depends(psycopg2_transaction)):
    sql = pgmini.Select(TaskPgmini.id, TaskPgmini.name, TaskPgmini.completed).From(
        TaskPgmini.Table
    )
    q, values = pgmini.build(sql, driver="psycopg")

    cursor.execute(q, values)
    result = cursor.fetchall()
    return [
        dict(id=id, name=name, completed=completed) for id, name, completed in result
    ]


@app.get("/pgmini-psycopg2/{id}", response_model=TaskDTO)
def get_pgmini_psycopg2(id: int, cursor=Depends(psycopg2_transaction)):
    sql = (
        pgmini.Select(TaskPgmini.id, TaskPgmini.name, TaskPgmini.completed)
        .From(TaskPgmini.Table)
        .Where(TaskPgmini.Table.id == id)
    )
    q, values = pgmini.build(sql, driver="psycopg")
    cursor.execute(q, values)
    id, name, completed = cursor.fetchone()
    return dict(id=id, name=name, completed=completed)


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


@app.get("/piccolo-transaction", response_model=list[bool])
async def list_piccolo_trancsction(_=Depends(piccolo_transaction)):
    return [True]


@app.get("/piccolo-transaction/{id}", response_model=bool)
async def get_piccolo_trancsction(id: int, _=Depends(piccolo_transaction)):
    return True


@app.get("/piccolo", response_model=List[TaskDTO])
async def list_piccolo(_=Depends(piccolo_transaction)):
    result = await TaskPiccolo.select().run()
    return result


@app.get("/piccolo/{id}", response_model=TaskDTO)
async def get_piccolo(id: int, _=Depends(piccolo_transaction)):
    result = await TaskPiccolo.select().where(TaskPiccolo.id == id).first().run()
    return result


@app.get("/peewee-no-pool", response_model=List[TaskDTO])
def list_peewee_no_pool(_=Depends(peewee_no_pool_transaction)):
    result = TaskPeeweeNoPool.select().dicts()
    return result


@app.get("/peewee-no-pool/{id}", response_model=TaskDTO)
def get_peewee_no_pool(id: int, _=Depends(peewee_no_pool_transaction)):
    result = TaskPeeweeNoPool.select().where(TaskPeeweeNoPool.id == id).dicts()
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


# Test response model validation -------------------------------------------------------


class Status(Enum):
    pending = 1
    done = 2
    error = 3


@dataclass(slots=True)
class DataclassResponse:
    id: int
    name: str
    status: Status
    created_at: datetime


class PydanticResponse(BaseModel):
    id: int
    name: str
    status: Status
    created_at: datetime


resp = [
    dict(id=id_, name=f"foo {id_}", status=Status.pending, created_at=datetime.now())
    for id_ in range(30)
]


@app.get("/no-resp-model")
async def list_no_model():
    return resp


@app.get("/no-resp-model/{id}")
async def get_no_model(id: int):
    return resp[id]


@app.get("/dict", response_model=list[dict])
async def list_dict():
    return resp


@app.get("/dict/{id}", response_model=dict)
async def get_dict(id: int):
    return resp[id]


@app.get("/dataclass", response_model=list[DataclassResponse])
async def list_dataclass():
    return resp


@app.get("/dataclass/{id}", response_model=DataclassResponse)
async def get_dataclass(id: int):
    return resp[id]


@app.get("/pydantic", response_model=list[PydanticResponse])
async def list_pydantic():
    return resp


@app.get("/pydantic/{id}", response_model=PydanticResponse)
async def get_pydantic(id: int):
    return resp[id]
