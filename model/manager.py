from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import engine, meta_data
from model.users import users

manager = Table("manager", meta_data,
             Column("id_mana", Integer, primary_key=True),
             Column("id_user", Integer, ForeignKey(users.c.id_user), nullable=False),
             Column("name_mana", String(50), nullable=False),
             Column("last_name", String(50), nullable=False)
             )

meta_data.create_all(engine)