

from pydantic import BaseModel
from models.user import User


class Deliverer(BaseModel):
    owner: User
    isVerified: bool
    stars: int
    reviews:list[str]
    currentLocation: str
    nationalID: str
    drivingLicense: str|None = None 
    