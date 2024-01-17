
from pydantic import BaseModel

from models.user import User

class FileMessage(BaseModel):
    #TODO: Change message to file path
    message:str
    ID: str
    isRead: bool
    timeSent:str
    fromUser:User
    toUser:User