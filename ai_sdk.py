from .service_endpoints import *
import requests

aiserviceurl = service_schema + ai_host + ai_apiurl

def get_Response(chatroom_uuid, message, cookie, headers):
    requests.get(url = aiserviceurl + '/system_response', params={'chatroom_uuid': chatroom_uuid, 'message': message, 'cookie': cookie}, headers=headers)
