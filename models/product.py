from pydantic import BaseModel
from models.specification import Specification
#from models.shop import Shop

class Product(BaseModel):
    name: str
    ID: str
    price: float
    tags: list[str]
    category:str
    imageUrl: str
    videoUrl: str|None = None
    numberInStock:int
    minimumOrder: int
    description: str
    productSpecifications:list[Specification]
    #shop: Shop
    
    
    
    
    
