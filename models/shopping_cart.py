
from pydantic import BaseModel
from models.product import Product

from models.user import User


class ShoppinCart(BaseModel):
    owner: User
    products:list[Product]
    totalPrice:float