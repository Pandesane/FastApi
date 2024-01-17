from pydantic import BaseModel

from models.user import User

class AudioMessage(BaseModel):
    #TODO: Change message to audio file path
    message:str
    ID: str
    isRead: bool
    timeSent:str
    fromUser:User
    toUser:User