from pydantic import BaseModel

"""Draft"""
class BaseRequest(BaseModel):
    cookie: str
    headers: dict = {}
