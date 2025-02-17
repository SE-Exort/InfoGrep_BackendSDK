from pydantic import BaseModel
import uuid;

class LoggerStruct(BaseModel):
    Endpoint: str
    Cookie: str
    User_UUID: str = None;
    File_UUID: str = None;
    Room_UUID: str = None;
