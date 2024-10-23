import psycopg2
from soupsieve import select
from sqlalchemy import MetaData, Column, String, Integer, Table, Result
from sqlalchemy import create_engine, select, insert, update, delete
from sqlalchemy.orm import create_session, Session, DeclarativeBase, mapped_column, Mapped


url="postgresql+psycopg2://postgres:pass@localhost/postgres"
engine = create_engine(url=url, echo=True)
session = create_session(bind=engine)
metadata= MetaData()

employees = Table(
        "employyes",
        metadata,
        Column("name", String),
        Column("age", Integer)
    )

with engine.connect() as conn:
    stmt = insert(employees).values(name="Bob", age=12)
    conn.execute(stmt)
    stmt = insert(employees).values(name="John", age=40)
    conn.execute(stmt)
    # stmt = insert(employees).values(name="Gaby", age=30)
    # conn.execute(stmt)
    # conn.commit()

with engine.connect() as conn:
    stmt = update(employees).where(employees.c.name=="Bob").values(age=15)
    conn.execute(stmt)
    # conn.commit()

with engine.connect() as conn:
    stmt = delete(employees).where(employees.c.name=="Gaby")
    conn.execute(stmt)
    # conn.commit()


with engine.connect() as conn:
    stmt = select(employees).order_by("age")
    res = conn.execute(stmt)
    for row in res:
        print(row)

