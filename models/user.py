from pydantic import BaseModel
from enum import Enum

class Gender(str,Enum):
    MALE = 'male'
    FEMALE = 'female'



class User(BaseModel):
    firstName:str
    lastName:str
    contact:str
    email:str
    location:str
    gender:Gender
    password:str