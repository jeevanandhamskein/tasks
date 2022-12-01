from sqlalchemy import create_engine,MetaData

engine = create_engine("mysql+mysqldb://root1234-ROOT:root@localhost:3306/secdb")
#engine=create_engine("mysql+mysqldb(pip:mysqlclient)://uname:password@localhost:3306/dbname")
conn=engine.connect()
meta=MetaData()