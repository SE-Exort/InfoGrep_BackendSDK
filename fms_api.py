from .service_endpoints import *
from .util import header_cleanup
import requests


fmsserviceurl = service_schema + fms_host + fms_apiurl

def fms_getFileList(chatroom_uuid, cookie, headers):
    return requests.get(url = fmsserviceurl + '/filelist', params={'chatroom_uuid': chatroom_uuid, 'cookie': cookie}, headers=header_cleanup(headers))

def fms_getFile(chatroom_uuid, file_uuid, cookie, headers):
    return requests.get(url = fmsserviceurl + '/file', params={'chatroom_uuid': chatroom_uuid, 'file_uuid': file_uuid, 'cookie': cookie}, headers=header_cleanup(headers))

def fms_postFile(chatroom_uuid, uploadedfile, cookie, headers):
    file = {'uploadedfile': open(uploadedfile, 'rb')}
    return requests.post(url = fmsserviceurl + '/file', params={'chatroom_uuid': chatroom_uuid, 'cookie': cookie}, files=file, headers=header_cleanup(headers))

def fms_deleteFile(chatroom_uuid, file_uuid, cookie, headers):
    return requests.delete(url = fmsserviceurl + '/file', params={'chatroom_uuid': chatroom_uuid, 'file_uuid': file_uuid, 'cookie': cookie}, headers=header_cleanup(headers))
