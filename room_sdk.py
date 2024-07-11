import requests
from fastapi import HTTPException

parseschema = 'http://'
parsehost = '127.0.0.1'
parseport = '8003'
parseapiurl = '/api'

parseserviceurl = parseschema + parsehost + ':' + parseport + parseapiurl
def get_userInRoom(chatroom_uuid, cookie):
    response = requests.get(url = parseserviceurl + '/userinroom', params={'chatroom_uuid': chatroom_uuid, 'cookie': cookie})
    if response.status_code != 200:
        raise HTTPException(status_code=400, detail="Unexpected response from Chatroom Service")
    if not response.json()['detail']:
        raise HTTPException(status_code=401, detail="User not in chatroom")
    return 
