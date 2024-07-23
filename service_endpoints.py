#This file configures the endpoints that services are located on

#Common definitions
service_schema = 'http://'
localhost_url = '127.0.0.1'

#Authentication service
auth_host = localhost_url
auth_port = '4000'

#Parsing Service
parse_host = localhost_url
parse_port = '8001'
parse_apiurl = '/api'

#File Management and Storage Service
fms_host = localhost_url
fms_port = '8002'
fms_apiurl = '/api'

#Chatroom Service
chatroom_host = localhost_url
chatroom_port = '8003'
chatroom_apiurl = '/api'

#AI Service
ai_host = localhost_url
ai_port = '8004'
ai_apiurl = '/api'

#Vector Storage Service
vectordb_host = localhost_url
vectordb_port = '8800'
vectordb_api_url = ''