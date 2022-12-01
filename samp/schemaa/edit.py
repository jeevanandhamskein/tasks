from pydantic import BaseModel

class upt_emp(BaseModel):
    emp_id:int
    emp_name:str
    place:str