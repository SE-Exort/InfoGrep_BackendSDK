from .service_endpoints import *
from .util import header_cleanup
import requests

aiserviceurl = service_schema + ai_host + ai_apiurl

def get_Response(chatroom_uuid, message, cookie, model, headers={}):
    requests.get(url = aiserviceurl + '/system_response', params={'chatroom_uuid': chatroom_uuid, 'message': message, 'cookie': cookie, 'model': model}, headers=header_cleanup(headers))
