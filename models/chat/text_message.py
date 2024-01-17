from pydantic import BaseModel

from models.user import User

class TextMessage(BaseModel):
    message:str
    ID: str
    isRead: bool
    timeSent:str
    fromUser:User
    toUser:User