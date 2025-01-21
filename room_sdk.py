from .service_endpoints import *
from .util import header_cleanup
import requests
from fastapi import HTTPException

chatroomserviceurl = service_schema + chatroom_host + chatroom_apiurl

def get_userInRoom(chatroom_uuid, cookie, headers):
    response = requests.get(url = chatroomserviceurl + '/userinroom', params={'chatroom_uuid': chatroom_uuid, 'cookie': cookie}, headers=header_cleanup(headers))
    if response.status_code != 200:
        raise HTTPException(status_code=400, detail="Unexpected response from Chatroom Service")
    if not response.json()['detail']:
        raise HTTPException(status_code=401, detail="User not in chatroom")
    return 

def post_message(chatroom_uuid, message, cookie, headers):
    return requests.post(url = chatroomserviceurl + '/message',  params={'chatroom_uuid': chatroom_uuid, 'cookie': cookie, 'message': message}, headers=header_cleanup(headers))
