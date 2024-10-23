from unicodedata import category

import psycopg2
from sqlalchemy import MetaData, Column, String, Integer, Table, Result, func
from sqlalchemy import create_engine, select, insert, update, delete
from sqlalchemy.orm import create_session, Session, DeclarativeBase, mapped_column, Mapped


url="postgresql+psycopg2://postgres:pass@localhost/postgres"
engine = create_engine(url=url, echo=False)
session = create_session(bind=engine)
metadata= MetaData()

products = Table(
        "products",
        metadata,
        Column("name", String),
        Column("category", String),
        Column("price", Integer),
        Column("amount", Integer),
    )

# metadata.create_all(engine)
with engine.connect() as conn:
    stmt = insert(products).values(
        name="toyota",
        category="car",
        price=1200,
        amount=100
    )
    conn.execute(stmt)
    stmt = insert(products).values(
        name="honda",
        category="car",
        price=1700,
        amount=80
    )
    conn.execute(stmt)
    stmt = insert(products).values(
        name="mitsubishi",
        category="car",
        price=900,
        amount=50
    )
    conn.execute(stmt)
    stmt = insert(products).values(
        name="toyota",
        category="car",
        price=1100,
        amount=40
    )
    conn.execute(stmt)
    # conn.commit()

with engine.connect() as conn:
    stmt = select(products.c.name, func.max(products.c.price)).group_by(products.c.name)
    conn.execute(stmt)
    print("max")
    for row in conn.execute(stmt):
        print(row)

with engine.connect() as conn:
    stmt = select(products.c.name, func.min(products.c.amount)).group_by(products.c.name)
    conn.execute(stmt)
    print("min")
    for row in conn.execute(stmt):
        print(row)
    
with engine.connect() as conn:
    stmt = select(products.c.name, func.sum(products.c.price)).group_by(products.c.name)
    conn.execute(stmt)
    print("sum")
    for row in conn.execute(stmt):
        print(row)

with engine.connect() as conn:
    stmt = select(products.c.name, func.count(products.c.name)).group_by(products.c.name)
    res = conn.execute(stmt)
    print("count")
    for row in conn.execute(stmt):
        print(row)

with engine.connect() as conn:
    stmt = select(products)
    res = conn.execute(stmt)
    print("all")
    for row in res:
        print(row)
