# encoding=utf-8
import requests
import json

params = {
    'username':'baiyong',
    'password':'baiyong'
}

response = requests.post('http://127.0.0.1:5000/api/users',json.dumps(params))
print(response.content)