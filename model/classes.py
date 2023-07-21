from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Numeric
from config.db import engine, meta_data
from model.professors import professors

classes = Table("classes", meta_data,
                Column("id_class", Integer, primary_key=True),
                Column("name_class", String(50), nullable=False),
                Column("level", String(50), nullable=False),
                Column("price", Numeric(precision=10, scale=2), nullable=False),
                Column("pack", String(50), nullable=False),
                Column("name_prof", String(50), nullable=False),
                Column("id_prof", Integer, ForeignKey(professors.c.id_prof), nullable=False)
                )

meta_data.create_all(engine)