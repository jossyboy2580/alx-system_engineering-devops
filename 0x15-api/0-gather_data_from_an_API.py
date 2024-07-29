#!/usr/bin/python3
"""
A module containing code to make a request to an
API endpoint
"""
from urllib import request
import json


def get_resp(value):
	"""
	A function that calls a task management API
	"""
        USERS_URL = f'https://jsonplaceholder.typicode.com/todos/(value)'
        TODOS_URL = f'https://jsonplaceholder.typicode.com/todos/{value}'

        user_response = request.urlopen(USERS_URL)
        if user_response.code == 200:
            aaa
        else:
            dddd
        resp = request.urlopen(URL).read()
        json_response = json.loads(resp)

