import requests
from typing import List, Union, Dict

vectordb_schema = 'http://'
vectordb_host = '127.0.0.1'
vectordb_port = '8800'
vectordb_api_url = ''

vectordb_service_url = vectordb_schema + vectordb_host + ':' + vectordb_port + vectordb_api_url
def vectordb_flush(collection: str):
    endpoint_url = f"{vectordb_service_url}/flush"
    body = {
        "collection": collection
    }
    resp = requests.post(url=endpoint_url, json=body)
    return resp

def vectordb_insert(collection: str, vector: List, args = Union[None|Dict]):
    """
    For the test collection, vector needs to be 256 len, and use 
    {
        "text": "test original string"
    }
    for args
    """
    endpoint_url = f"{vectordb_service_url}/insert"
    body = {
        "collection": collection,
        "vector": vector,
        "args": args
    }
    resp = requests.post(url=endpoint_url, json=body)
    return resp

def vectordb_search(collection: str, vector: List, args = Union[None|Dict]):
    endpoint_url = f"{vectordb_service_url}/search"
    body = {
        "collection": collection,
        "vector": vector,
        "args": args
    }
    resp = requests.post(url=endpoint_url, json=body)
    return resp

def vectordb_get_collection(collection: str):
    endpoint_url = f"{vectordb_service_url}/setting/collection"
    body = {
        "collection": collection
    }
    resp = requests.get(url=endpoint_url, json=body)
    return resp

def vectordb_get_num_data(collection: str):
    endpoint_url = f"{vectordb_service_url}/setting/num_data"
    body = {
        "collection": collection
    }
    resp = requests.get(url=endpoint_url, json=body)
    return resp

def vectordb_delete_data(collection: str, expr: str):
    endpoint_url = f"{vectordb_service_url}/delete/data"
    body = {
        "collection": collection,
        "expr": expr
    }
    resp = requests.delete(url=endpoint_url, json=body)
    return resp

def vectordb_delete_collection(collection: str):
    endpoint_url = f"{vectordb_service_url}/delete/collection"
    body = {
        "collection": collection
    }
    resp = requests.delete(url=endpoint_url, json=body)
    return resp
