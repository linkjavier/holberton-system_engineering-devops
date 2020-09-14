#!/usr/bin/python3
""" Script to export data in the JSON format.
"""

import requests
from sys import argv
import json


if __name__ == "__main__":

    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(argv[1]))
    name = user.json().get('name')
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = todos.json()
    todosuser = {}
    list_task = []

    for task in todos:
        if task.get('userId') == int(argv[1]):
            toDict = {"task": task.get('title'),
                      "completed": task.get('completed'),
                      "username": user.json().get('name')}
            list_task.append(toDict)
    todosuser[argv[1]] = list_task

    filename = argv[1] + '.json'
    with open(filename, mode='w') as jsonfile:
        json.dump(todosuser, jsonfile)
