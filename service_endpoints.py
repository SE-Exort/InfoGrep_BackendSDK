#This file configures the endpoints that services are located on
import os

#Common definitions
service_schema = 'http://'
localhost_url = '127.0.0.1'

#Authentication service
auth_port = '4000'
auth_host = os.environ.get("AUTH_SERVICE_HOST", f"{localhost_url}:{auth_port}")
auth_apiurl = ''

#Parsing Service
parse_port = '8001'
parse_host = os.environ.get("PARSING_SERVICE_HOST", f"{localhost_url}:{parse_port}")
parse_apiurl = '/api'

#File Management and Storage Service
fms_port = '8002'
fms_host = os.environ.get("FILE_MANAGEMENT_SERVICE_HOST", f"{localhost_url}:{fms_port}")
fms_apiurl = '/api'

#Chatroom Service
chatroom_port = '8003'
chatroom_host = os.environ.get("CHATROOM_SERVICE_HOST", f"{localhost_url}:{chatroom_port}")
chatroom_apiurl = '/api'

#AI Service
ai_port = '8004'
ai_host = os.environ.get("AI_SERVICE_HOST", f"{localhost_url}:{ai_port}")
ai_apiurl = '/api'

#Vector Storage Service
vectordb_port = '8800'
vectordb_host = os.environ.get("VECTOR_MANAGEMENT_SERVICE_HOST", f"{localhost_url}:{vectordb_port}")
vectordb_api_url = ''

#Video Service
video_port = '8879'
video_host = os.environ.get("VIDEO_SERVICE_HOST", f"{localhost_url}:{video_port}")
video_api_url = ''