import requests
from fastapi import HTTPException

chatroomschema = 'http://'
chatroomhost = '127.0.0.1'
chatroomport = '8003'
chatroomapiurl = '/api'

chatroomserviceurl = chatroomschema + chatroomhost + ':' + chatroomport + chatroomapiurl
def get_userInRoom(chatroom_uuid, cookie):
    response = requests.get(url = chatroomserviceurl + '/userinroom', params={'chatroom_uuid': chatroom_uuid, 'cookie': cookie})
    if response.status_code != 200:
        raise HTTPException(status_code=400, detail="Unexpected response from Chatroom Service")
    if not response.json()['detail']:
        raise HTTPException(status_code=401, detail="User not in chatroom")
    return 

def post_message(chatroom_uuid, message, cookie):
    return requests.post(url = chatroomserviceurl + '/message',  params={'chatroom_uuid': chatroom_uuid, 'cookie': cookie, 'message': message})
