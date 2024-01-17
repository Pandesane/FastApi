from pydantic import BaseModel
#from models.shop import Shop

from models.specification import Specification
class Service(BaseModel):
    name: str
    ID: str
    price: float
    tags: list[str]
    category:str
    imageUrl: str
    videoUrl: str|None = None
    description: str
    serviceSpecifications:list[Specification]
    #shop: Shop