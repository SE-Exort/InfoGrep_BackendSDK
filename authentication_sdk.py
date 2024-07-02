import requests
import json

URL = 'http://localhost:4000'

class User:
    def __init__(self, token) -> None:
        self.token = token
        if not self.is_valid():
            raise Exception('Invalid session token') 
    
    def is_valid(self) -> bool:
        response = requests.post(f'{URL}/check', {'sessionToken': self.token})
        response_dict = json.loads(response.text)

        if response_dict['error'] or not response_dict["data"]: return False
        
        self.username = response_dict["data"]
        
        return True
    
    def profile(self):
        return {
            'username': self.username
        }

class Authentication:
    @staticmethod
    def login(username, password):
        response = requests.post(f'{URL}/login', {'username': username, 'password': password})
        response_dict = json.loads(response.text)

        if response_dict['error']:
            raise Exception(response_dict['status'])
        else:
            return User(response_dict['data'])
        
    
    @staticmethod
    def register(username, password):
        response = requests.post(f'{URL}/register', {'username': username, 'password': password})
        response_dict = json.loads(response.text)

        if response_dict['error']:
            raise Exception(response_dict['status'])
        else:
            return User(response_dict['data'])
        

