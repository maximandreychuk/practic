from datetime import datetime, time

from sqlalchemy import MetaData, Column, Integer, Table, Result, ForeignKey, Text, String, DateTime
from sqlalchemy import create_engine, select, insert, update, delete
from sqlalchemy.orm import create_session, Session, DeclarativeBase, mapped_column, Mapped


url="postgresql+psycopg2://postgres:pass@localhost/postgres"
engine = create_engine(url=url, echo=False)
session = create_session(bind=engine)
metadata= MetaData()

# drivers = Table(
#     "drivers",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("name", String, unique=True),
# )
#
# cars = Table(
#     "cars",
#     metadata,
# Column("id", Integer, primary_key=True),
#     Column("drivers_id", ForeignKey("drivers.id"), nullable=False),
#     Column("name", String),
#     Column("release", DateTime, index=True),
#     Column("horsepower", Integer,)
#     )


# metadata.create_all(engine)
# with engine.connect() as conn:
#     stmt = insert(drivers).values(id=2, name="Bob")
#     conn.execute(stmt)
    # conn.commit()

# with engine.connect() as conn:
    # stmt = insert(cars).values(id=1, drivers_id=1, name="toyota", release=datetime.now(), horsepower=210)
    # conn.execute(stmt)
    # stmt = insert(cars).values(id=2, drivers_id=1, name="honda", release=datetime.now(), horsepower=159)
    # conn.execute(stmt)
    # conn.commit()
# with engine.connect() as conn:
#     stmt = select(cars).join(drivers, cars.c.drivers_id == drivers.c.id).where(cars.c.name=="toyota")
#     for row in conn.execute(stmt):
#         print(row)


# INDEXES
nums = Table(
    "nums",
    metadata,
    Column("one", Integer),
    Column("two", Integer, index=True)
)
metadata.create_all(engine)



# with engine.connect() as conn:
    # for i in range(0,100000000):
    #     stmt = insert(nums).values(one=i)
    #     conn.execute(stmt)
    #     conn.commit()
    # for i in range(0, 102231):
    #     stmt = insert(nums).values(two=i)
    #     conn.execute(stmt)
    #     conn.commit()

start_time = datetime.now()
with engine.connect() as conn:
    stmt = select(nums).where(nums.c.one > 102230)
    res = conn.execute(stmt)
    for row in res:
        print(row)
end_time = datetime.now()
print(f"Время выполнения без индексом: {end_time - start_time} секунд")

# Запрос без индекса
start_time = datetime.now()
with engine.connect() as conn:
    stmt = select(nums).where(nums.c.two > 102230)
    res = conn.execute(stmt)
    for row in res:
        print(row)
end_time = datetime.now()
print(f"Время выполнения с индекса: {end_time - start_time} секунд")



