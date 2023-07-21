from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer
from config.db import engine, meta_data
from model.discount import discount
from model.students import students

student_discount = Table("student_discount", meta_data,
                Column("id_student_discount", Integer, primary_key=True),
                Column("id_discount", Integer, ForeignKey(discount.c.id_discount)),
                Column("id_student", Integer, ForeignKey(students.c.id_student))
                )

meta_data.create_all(engine)