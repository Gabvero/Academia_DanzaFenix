from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import engine, meta_data

discount = Table("discount", meta_data,
                 Column("id_discount", Integer, primary_key=True),
                 Column("discount_percent", Integer),
                 Column("discount_type", String(50))
                )

meta_data.create_all(engine)