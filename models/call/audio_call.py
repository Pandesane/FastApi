
from pydantic import BaseModel


class AudioCall(BaseModel):
   
    audioStream:str
    communicationChannel:str
    isOnHold:bool
    hasHangUp:bool
    timeInCall: str
    productOfInterestID:str
    #TODO: Change AudioCallState to an enum
    audioCallState:str
    