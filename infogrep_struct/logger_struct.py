from pydantic import BaseModel
import uuid;

class LoggerStruct(BaseModel):
    Endpoint: str
    Cookie: str
    User_UUID: str
    File_UUID: str
    Room_UUID: str
