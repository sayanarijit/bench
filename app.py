from dataclasses import dataclass
from typing import List

import peewee
import sqlalchemy as sa
from fastapi import FastAPI
from piccolo import columns as picols
from piccolo.table import Table as PiccoloTable
from sqla_fancy_core import TableFactory
from sqlalchemy.ext.asyncio import create_async_engine

import piccolo_conf

# Peewee -------------------------------------------------------------------------------
peewee_state_default = {"closed": None, "conn": None, "ctx": None, "transactions": None}
peeweedb = peewee.PostgresqlDatabase(
    "postgres", user="dev", password="dev", host="localhost", port=5432
)


class TaskPeewee(peewee.Model):
    name = peewee.CharField()
    completed = peewee.BooleanField()

    class Meta:
        database = peeweedb
        table_name = "task"


# Sqlalchemy ---------------------------------------------------------------------------

tf = TableFactory()
sqla_psycopg2_engine = sa.create_engine(
    "postgresql+psycopg2://dev:dev@localhost/postgres"
)


sqla_asyncpg_engine = create_async_engine(
    "postgresql+asyncpg://dev:dev@localhost/postgres"
)


class TaskSqla:
    id = tf.auto_id()
    name = tf.string("name")
    completed = tf.boolean("completed")

    Table = tf("task")


# Piccolo ------------------------------------------------------------------------------

piccolodb = piccolo_conf.DB


class TaskPiccolo(PiccoloTable, tablename="task"):
    id = picols.Integer(primary_key=True, auto_increment=True)
    name = picols.Varchar()
    completed = picols.Boolean()


# --------------------------------------------------------------------------------------


@dataclass
class TaskDTO:
    id: int
    name: str
    completed: bool


app = FastAPI()


@app.on_event("startup")
async def startup():
    peeweedb.create_tables([TaskPeewee])
    await piccolodb.start_connection_pool()


@app.get("/sqla-asyncpg", response_model=List[TaskDTO])
async def list_sqla_asyncpg():
    async with sqla_asyncpg_engine.begin() as session:
        result = await session.execute(sa.select(TaskSqla.Table))
        return list(result.mappings())


@app.get("/sqla-asyncpg/{id}", response_model=TaskDTO)
async def get_sqla_asyncpg(id: int):
    async with sqla_asyncpg_engine.begin() as session:
        result = await session.execute(
            sa.select(TaskSqla.Table).where(TaskSqla.id == id)
        )
        return next(result.mappings())


@app.get("/sqla-asyncpg-create/", response_model=int)
async def create_sqla_asyncpg(name: str) -> int:
    async with sqla_asyncpg_engine.begin() as session:
        result = await session.execute(
            sa.insert(TaskSqla.Table)
            .values({TaskSqla.name: name, TaskSqla.completed: True})
            .returning(TaskSqla.id)
        )
        return result.scalar_one()


@app.get("/sqla-psycopg2", response_model=List[TaskDTO])
def list_sqla_psycopg2():
    with sqla_psycopg2_engine.begin() as session:
        result = session.execute(sa.select(TaskSqla.Table))
        return list(result.mappings())


@app.get("/sqla-psycopg2/{id}", response_model=TaskDTO)
def get_sqla_psycopg2():
    with sqla_psycopg2_engine.begin() as session:
        result = session.execute(sa.select(TaskSqla.Table).where(TaskSqla.id == 1))
        return next(result.mappings())


@app.get("/peewee", response_model=List[TaskDTO])
def list_peewee():
    with peeweedb.transaction():
        with peeweedb.atomic():
            result = TaskPeewee.select()
            return list(result.dicts())


@app.get("/peewee/{id}", response_model=TaskDTO)
def get_peewee(id: int):
    with peeweedb.transaction():
        with peeweedb.atomic():
            result = TaskPeewee.select().where(TaskPeewee.id == id)
            return result.dicts()[0]


@app.get("/peewee-create/", response_model=int)
def create_peewee(name: str) -> int:
    with peeweedb.transaction():
        with peeweedb.atomic():
            result = TaskPeewee.insert(name=name, completed=False).execute()
            return result


@app.get("/piccolo", response_model=List[TaskDTO])
async def list_piccolo():
    async with piccolodb.transaction():
        result = await TaskPiccolo.select().run()
        return list(result)


@app.get("/piccolo/{id}", response_model=TaskDTO)
async def get_piccolo(id: int):
    async with piccolodb.transaction():
        result = await TaskPiccolo.select().where(TaskPiccolo.id == id).run()
        return result[0]
