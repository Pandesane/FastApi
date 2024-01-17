from pydantic import BaseModel

class Specification(BaseModel):
    name:str
    value:str