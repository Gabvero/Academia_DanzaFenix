from sqlalchemy import Table, Column, ForeignKey, CheckConstraint, text
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import engine, meta_data
from model.users import users
from model.inscriptions import inscriptions



students = Table(
    "students", meta_data,
    Column("id_student", Integer, primary_key=True),
    Column("id_user", Integer, ForeignKey(users.c.id_user), nullable=False),
    Column("id_inscription", Integer, ForeignKey(inscriptions.c.id_inscription), nullable=False),
    Column("name_student", String(50), nullable=False),
    Column("last_name_student", String(50), nullable=False),
    Column("age", Integer, CheckConstraint('age < 100'), nullable=False),
    Column("phone", String(9), nullable=False),
    Column("email", String(100))
)

meta_data.create_all(engine)