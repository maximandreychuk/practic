from datetime import datetime, time

from click.formatting import measure_table
from sqlalchemy import MetaData, Column, Integer, Table, Result, ForeignKey, Text, String, DateTime
from sqlalchemy import create_engine, select, insert, update, delete
from sqlalchemy.orm import create_session, Session, DeclarativeBase, mapped_column, Mapped


url="postgresql+psycopg2://postgres:pass@localhost/postgres"
engine = create_engine(url=url, echo=False)
session = create_session(bind=engine)
metadata= MetaData()

goods = Table(
        "goods",
        metadata,
        Column("name", String),
        Column("amount", Integer)
    )
metadata.create_all(engine)


with engine.connect() as conn:
    stmt = insert(goods).values(
        name="water",
        amount=5
    )
    conn.execute(stmt)
    stmt = insert(goods).values(
        name="chokolade",
        amount=5
    )
    conn.execute(stmt)
    stmt = insert(goods).values(
        name="fish",
        amount=0
    )
    conn.execute(stmt)
    # conn.commit()

with engine.connect() as conn:
    water_amount_stmt = [i[0] for i in conn.execute(select(goods.c.amount).where(goods.c.name=="water"))][0]
    fish_amount_stmt = [i[0] for i in conn.execute(select(goods.c.amount).where(goods.c.name=="fish"))][0]
    if water_amount_stmt < 1 or fish_amount_stmt < 1:
        conn.rollback()
    else:
        new_fish_amount_stmt = update(goods).where(goods.c.name=="water").values(amount=water_amount_stmt-1)
        conn.execute(new_fish_amount_stmt)
        new_water_amount_stmt = update(goods).where(goods.c.name=="fish").values(amount=fish_amount_stmt-1)
        conn.execute(new_water_amount_stmt)
        conn.commit()

with engine.connect() as conn:
    stmt = select(goods)
    for row in conn.execute(stmt):
        print(row)



