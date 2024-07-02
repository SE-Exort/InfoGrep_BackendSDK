import requests
import json

URL = 'http://localhost:4000'

class User:
    def __init__(self, token) -> None:
        response = requests.post(f'{URL}/check', {'sessionToken': token})
        response_dict = json.loads(response.text)

        if response_dict['error']:
            raise Exception('Invalid session token')
        else:
            self.username = response_dict["data"]
    
    def __init__(self, token) -> None:
        response = requests.post(f'{URL}/check', {'sessionToken': token})
        response_dict = json.loads(response.text)

        if response_dict['error']:
            raise Exception('Invalid session token')
        else:
            self.username = response_dict["data"]
    
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
        

