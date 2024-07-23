import requests

aischema = 'http://'
aihost = '127.0.0.1'
aiport = '8004'
aiapiurl = '/api'

aiserviceurl = aischema + aihost + ':' + aiport + aiapiurl
def get_Response(chatroom_uuid, message, cookie):
    requests.get(url = aiserviceurl + '/system_response', params={'chatroom_uuid': chatroom_uuid, 'message': message, 'cookie': cookie})
