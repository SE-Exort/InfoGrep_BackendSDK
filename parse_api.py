from .service_endpoints import *
import requests


parseserviceurl = service_schema + parse_host + parse_apiurl
def parse_postStartParsing(chatroom_uuid, file_uuid, filetype, cookie):
    return requests.post(url = parseserviceurl + '/start_parsing', params={'chatroom_uuid': chatroom_uuid, 'file_uuid': file_uuid, 'filetype': filetype, 'cookie': cookie})

def parse_postCancelParsing(chatroom_uuid, file_uuid, cookie):
    return requests.post(url = parseserviceurl + '/cancel_parsing', params={'chatroom_uuid': chatroom_uuid, 'file_uuid': file_uuid, 'cookie': cookie})

def parse_getParsingStatus(chatroom_uuid, file_uuid, cookie):
    return requests.get(url = parseserviceurl + '/parsing_status', params={'chatroom_uuid': chatroom_uuid, 'file_uuid': file_uuid, 'cookie': cookie})
