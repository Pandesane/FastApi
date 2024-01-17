from pydantic import BaseModel

from models.product import Product
from models.service import Service
from models.user import User


class Shop(BaseModel):
    owner : User
    products:list[Product]
    services:list[Service]
    
    