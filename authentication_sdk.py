from .service_endpoints import *
import requests
import json
from fastapi import HTTPException

URL = service_schema+auth_host+ ':' + auth_port
class User:
    def __init__(self, token) -> None:
        self.token = token
        if not self.is_valid():
            raise HTTPException(status_code= 401, detail="User or session cookie invalid") 
    
    def is_valid(self) -> bool:
        response = requests.post(f'{URL}/check', json={'sessionToken': self.token})
        response_dict = json.loads(response.text)        

        if "error" in response_dict: return False
                
        #self.username = response_dict["data"]['username']
        self.user_uuid = response_dict["data"]['id']
        
        return True
    
    def profile(self):
        return {
            #'username': self.username,
            'user_uuid': self.user_uuid
        }

class Authentication:
    @staticmethod
    def login(username, password):
        response = requests.post(f'{URL}/login', json={'username': username, 'password': password})
        response_dict = json.loads(response.text)

        print(response_dict)
        if response_dict['error']:
            raise Exception(response_dict['status'])
        else:
            return User(response_dict['data'])
        
    
    @staticmethod
    def register(username, password):
        response = requests.post(f'{URL}/register', json={'username': username, 'password': password})
        response_dict = json.loads(response.text)

        if response_dict['error']:
            raise Exception(response_dict['status'])
        else:
            return User(response_dict['data'])
        

