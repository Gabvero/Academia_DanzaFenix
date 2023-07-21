from sqlalchemy import Table, Column, ForeignKey, CheckConstraint, text
from sqlalchemy.sql.sqltypes import Integer, String, Boolean, Date, Numeric
from config.db import engine, meta_data
from model.users import users
from model.classes import classes
from datetime import timedelta

inscriptions = Table(
    "inscriptions", meta_data,
    Column("id_inscription", Integer, primary_key=True),
    Column("id_user", Integer, ForeignKey(users.c.id_user), nullable=False),
    Column("id_class", Integer, ForeignKey(classes.c.id_class), nullable=False),
    Column("type_inscription", String(50), nullable=False),
    Column("status", Boolean, nullable=False),
    Column("start_date", Date, nullable=False),
    Column("finish_date", Date, nullable=False, default=text("(start_date + INTERVAL 1 MONTH)")),
    Column("total_price", Numeric(precision=10, scale=2), nullable=False)
)

meta_data.create_all(engine)