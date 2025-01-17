from .service_endpoints import *
import requests


fmsserviceurl = service_schema + fms_host + fms_apiurl
def fms_getFileList(chatroom_uuid, cookie):
    return requests.get(url = fmsserviceurl + '/filelist', params={'chatroom_uuid': chatroom_uuid, 'cookie': cookie})

def fms_getFile(chatroom_uuid, file_uuid, cookie):
    return requests.get(url = fmsserviceurl + '/file', params={'chatroom_uuid': chatroom_uuid, 'file_uuid': file_uuid, 'cookie': cookie})

def fms_postFile(chatroom_uuid, uploadedfile, cookie):
    file = {'uploadedfile': open(uploadedfile, 'rb')}
    return requests.post(url = fmsserviceurl + '/file', params={'chatroom_uuid': chatroom_uuid, 'cookie': cookie}, files=file)

def fms_deleteFile(chatroom_uuid, file_uuid, cookie):
    return requests.delete(url = fmsserviceurl + '/file', params={'chatroom_uuid': chatroom_uuid, 'file_uuid': file_uuid, 'cookie': cookie})
