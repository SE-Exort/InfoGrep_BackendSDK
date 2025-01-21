from .service_endpoints import *
from .util import header_cleanup
import requests


parseserviceurl = service_schema + parse_host + parse_apiurl

def parse_postStartParsing(chatroom_uuid, file_uuid, filetype, cookie, headers):
    return requests.post(url = parseserviceurl + '/start_parsing', params={'chatroom_uuid': chatroom_uuid, 'file_uuid': file_uuid, 'filetype': filetype, 'cookie': cookie}, headers=header_cleanup(headers))

def parse_postCancelParsing(chatroom_uuid, file_uuid, cookie, headers):
    return requests.post(url = parseserviceurl + '/cancel_parsing', params={'chatroom_uuid': chatroom_uuid, 'file_uuid': file_uuid, 'cookie': cookie}, headers=header_cleanup(headers))

def parse_getParsingStatus(chatroom_uuid, file_uuid, cookie, headers):
    return requests.get(url = parseserviceurl + '/parsing_status', params={'chatroom_uuid': chatroom_uuid, 'file_uuid': file_uuid, 'cookie': cookie}, headers=header_cleanup(headers))
