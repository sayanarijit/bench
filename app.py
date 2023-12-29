from dataclasses import dataclass
from typing import List

import peewee
import sqlalchemy as sa
import sqlalchemy.orm
from fastapi import FastAPI
from piccolo.columns import Integer, Varchar
from piccolo.table import Table
from sqla_fancy_core import TableFactory
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from piccolo_conf import DB

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

sqla_psycopg2_sessionmaker = sqlalchemy.orm.sessionmaker(sqla_psycopg2_engine)

sqla_asyncpg_engine = create_async_engine(
    "postgresql+asyncpg://dev:dev@localhost/postgres"
)

sqla_asyncpg_sessionmaker = async_sessionmaker(sqla_asyncpg_engine)


class TaskSqla:
    id = tf.auto_id()
    name = tf.string("name")
    completed = tf.boolean("completed")

    Table = tf("task")


# Piccolo ------------------------------------------------------------------------------
class TaskPiccolo(Table, tablename="task"):
    id = Integer(primary_key=True)
    name = Varchar()
    completed = Integer()


@dataclass
class TaskDTO:
    name: str
    completed: bool


app = FastAPI()


@app.on_event("startup")
def startup():
    peeweedb.create_tables([TaskPeewee])


@app.get("/sqla-asyncpg", response_model=List[TaskDTO])
async def list_sqla_asyncpg():
    async with sqla_asyncpg_sessionmaker() as session:
        result = await session.execute(sa.select(TaskSqla.Table))
        return list(result.mappings())


@app.get("/sqla-psycopg2", response_model=List[TaskDTO])
def list_sqla_psycopg2():
    with sqla_psycopg2_sessionmaker() as session:
        result = session.execute(sa.select(TaskSqla.Table))
        return list(result.mappings())


@app.get("/peewee", response_model=List[TaskDTO])
def list_peewee():
    with peeweedb.transaction():
        result = TaskPeewee.select().dicts()
        return list(result)


@app.get("/piccolo", response_model=List[TaskDTO])
async def list_piccolo():
    async with DB.transaction():
        result = await TaskPiccolo.select().run()
        return list(result)
