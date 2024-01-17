

from pydantic import BaseModel
from models.product import Product
from models.service import Service


class SectionModel(BaseModel):
    sectionName:str
    sectionCategory:str
    products:list[Product]
    services:list[Service]
    #TODO: Add section the contains food and restuarants
    