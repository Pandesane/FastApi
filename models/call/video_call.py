
from pydantic import BaseModel


class VideoCall(BaseModel):
    videoStream:str
    audioStream:str
    communicationChannel:str
    isOnHold:bool
    hasHangUp:bool
    timeInCall: str
    productOfInterestID:str
    #TODO: Change VideoCallState to an enum
    videoCallState:str
    