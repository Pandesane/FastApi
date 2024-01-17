


from pydantic import BaseModel
from models.product import Product


class PackageModel(BaseModel):
    packageName:str
    packageImage:str
    totalPrice:float
    products:list[Product]