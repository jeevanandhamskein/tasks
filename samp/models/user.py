from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer,String
from config.db import meta,engine

employee=Table("employee",meta,Column(
    "emp_id",Integer,primary_key=True),
    Column("emp_name",String(255)),
    Column("place",String(255))
)

meta.create_all(engine)
