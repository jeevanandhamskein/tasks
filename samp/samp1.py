from fastapi import FastAPI
from config.db import conn 
from models.user import employee
from schemaa.user import newu
from schemaa.edit import upt_emp
 

app=FastAPI()


@app.get('/')
def welcome():
    return ("hello world")


@app.post('/add_emp')
async def create_user(user:newu):
    new_emp= {"emp_id":user.emp_id,"emp_name":user.emp_name,"place":user.place}
    ids=conn.execute(
        employee.select().where(employee.c.emp_id==user.emp_id)
    ).first()
    if ids:
        return {"already exist"}

    else:
        conn.execute(employee.insert().values(new_emp))
        id=conn.execute(
            employee.select().where(employee.c.emp_id == user.emp_id)
        ).first()
        if id:
            return {"added"}



@app.get('/getemp')
async def get_emp(id:int):
    info=conn.execute(employee.select().where(employee.c.emp_id==id)).first()
    if info:
        return info
    else:
        return "data not found"  


@app.put('/update')
def update(id:int,edit:upt_emp):

    id=conn.execute(
            employee.select().where(employee.c.emp_id==id)).first()
            
    if id:
        conn.execute(employee.update()
        .where(employee.c.emp_id==id)
        .values(emp_id=edit.emp_id,emp_name=edit.emp_name,place=edit.place)
        )
        return "updated"

    else:
        return "data not found"




@app.delete('/delete')
async def del_emp(id:int):
    idss=conn.execute(employee.select().where(employee.c.emp_id==id)).first()
    if idss:
        conn.execute(
            employee.delete().where(employee.c.emp_id==id)
        )
        return {"deleted"}
    else:
        return {"data not found"}        















