from pydantic import BaseModel
from user import User
from product import Product
from service import Service

class StartUp(BaseModel):
    owner : User
    startUpName : str
    ID:str
    category: str
    description: str
    imageUrl: str
    videoUrl: list[str]
    products:list[Product]
    services:list[Service]
    #TODO: Add Investmaent amount
    