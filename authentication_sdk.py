from .service_endpoints import *
from .util import header_cleanup
import requests
import json
from fastapi import HTTPException

URL = service_schema + auth_host + auth_apiurl
class User:
    def __init__(self, token, headers={}) -> None:
        self.token = token
        self.headers = header_cleanup(headers)
        self.user_uuid = ""
        self.is_admin = False
        
        if not self.is_valid():
            raise HTTPException(status_code= 401, detail="User or session cookie invalid") 
    
    def is_valid(self) -> bool:
        response = requests.post(f'{URL}/check', json={'sessionToken': self.token}, headers=self.headers)
        response_dict = json.loads(response.text)        

        if response_dict["error"]: return False
                
        #self.username = response_dict["data"]['username']
        self.user_uuid = response_dict['id']
        self.is_admin = response_dict['is_admin']
        return True
    
    def profile(self):
        return {
            #'username': self.username,
            'user_uuid': self.user_uuid,
            'is_admin': self.is_admin
        }

class Authentication:
    @staticmethod
    def login(username, password, headers={}):
        response = requests.post(f'{URL}/login', json={'username': username, 'password': password}, headers=headers)
        response_dict = json.loads(response.text)

        print(response_dict)
        if response_dict['error']:
            raise Exception(response_dict['status'])
        else:
            return User(response_dict['data'])
        
    
    @staticmethod
    def register(username, password, headers={}):
        response = requests.post(f'{URL}/register', json={'username': username, 'password': password}, headers=headers)
        response_dict = json.loads(response.text)

        if response_dict['error']:
            raise Exception(response_dict['status'])
        else:
            return User(response_dict['data'])
        

