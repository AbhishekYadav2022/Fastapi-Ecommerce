# from datetime import datetime
from pydantic import BaseModel, EmailStr

# Schema For Creating User 
class CreateUser(BaseModel):
    id: str
    first_name: str
    last_name: str
    email: EmailStr
    phone: int
    password: str
    # class Config:
    #     orm_mode = True