from pydantic import BaseModel
from user import User
from product import Product
from service import Service

class Company(BaseModel):
    owner : User
    companyName : str
    ID:str
    category: str
    description: str
    imageUrl: str
    videoUrl: str
    products:list[Product]
    services:list[Service]
    