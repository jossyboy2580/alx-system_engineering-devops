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
    USERS_URL = f'https://jsonplaceholder.typicode.com/todos/{value}'
    TODOS_URL = f'https://jsonplaceholder.typicode.com/todos/?userId={value}'
    user_response = request.urlopen(USERS_URL)
    if user_response.code == 200:
        content = json.loads(user_response.read())
        name = content["name"]
        t_resp = request.urlopen(TODOS_URL)
        if t_resp.code == 200:
            todos = json.loads(t_res.read())
            total = len(todos)
            done = []
            for i in range(len(todos)):
                if todos[i]['completed']:
                    done.append(i)
            print(f'Employee {name} is done with tasks({len(done)}/{total})')
            for i in done:
                print(f'     {todos[i]["title"]}')
    else:
        return


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        get_resp(sys.argv[1])
