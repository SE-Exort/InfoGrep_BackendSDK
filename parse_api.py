import requests

parseschema = 'http://'
parsehost = '127.0.0.1'
parseport = '8001'
parseapiurl = '/api'

parseserviceurl = parseschema + parsehost + ':' + parseport + parseapiurl
def parse_postStartParsing(user_uuid, chatroom_uuid, file_uuid, filetype, cookie):
    return requests.post(url = parseserviceurl + '/start_parsing', params={'user_uuid': user_uuid, 'chatroom_uuid': chatroom_uuid, 'file_uuid': file_uuid, 'filetype': filetype, 'cookie': cookie})

def parse_postCancelParsing(user_uuid, chatroom_uuid, file_uuid, cookie):
    return requests.post(url = parseserviceurl + '/cancel_parsing', params={'user_uuid': user_uuid, 'chatroom_uuid': chatroom_uuid, 'file_uuid': file_uuid, 'cookie': cookie})

def parse_getParsingStatus(user_uuid, chatroom_uuid, file_uuid, cookie):
    return requests.get(url = parseserviceurl + '/parsing_status', params={'user_uuid': user_uuid, 'chatroom_uuid': chatroom_uuid, 'file_uuid': file_uuid, 'cookie': cookie})
