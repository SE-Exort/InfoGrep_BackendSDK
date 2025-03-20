from .service_endpoints import *
from .util import header_cleanup
import requests

aiserviceurl = service_schema + ai_host + ai_apiurl

def get_Response(chatroom_uuid, history, message, sessionToken, chat_model, embedding_model, chat_provider, embedding_provider, headers={}):
    json_body = {'history': history,
                'chatroom_uuid': chatroom_uuid,
                'message': message,
                'sessionToken': sessionToken,
                'chat_model': chat_model,
                'embedding_model': embedding_model,
                'chat_provider': chat_provider,
                'embedding_provider': embedding_provider}
    print(json_body)
    return requests.post(url = aiserviceurl + '/system_response', json=json_body, headers=header_cleanup(headers)).json()

def parse_postStartParsing(chatroom_uuid, file_uuid, filetype, cookie, headers={}):
    return requests.post(url = aiserviceurl + '/start_parsing', params={'chatroom_uuid': chatroom_uuid, 'file_uuid': file_uuid, 'filetype': filetype, 'cookie': cookie}, headers=header_cleanup(headers))

def parse_postCancelParsing(chatroom_uuid, file_uuid, cookie, headers={}):
    return requests.post(url = aiserviceurl + '/cancel_parsing', params={'chatroom_uuid': chatroom_uuid, 'file_uuid': file_uuid, 'cookie': cookie}, headers=header_cleanup(headers))

def parse_getParsingStatus(chatroom_uuid, file_uuid, cookie, headers={}):
    return requests.get(url = aiserviceurl + '/parsing_status', params={'chatroom_uuid': chatroom_uuid, 'file_uuid': file_uuid, 'cookie': cookie}, headers=header_cleanup(headers))

def get_supported_filetypes(headers={}):
    return requests.get(url = aiserviceurl + '/file_types', headers=header_cleanup(headers))