#!/usr/bin/python3
""" Script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress.
"""

import json
import requests
from sys import argv


if __name__ == "__main__":

    users = requests.get('https://jsonplaceholder.typicode.com/users')
    users = users.json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = todos.json()
    all_todos = {}

    for user in users:
        list_task = []
        for task in todos:
            if task.get('userId') == user.get('id'):
                toDict = {"username": user.get('username'),
                          "task": task.get('title'),
                          "completed": task.get('completed')}
                list_task.append(toDict)
        all_todos[user.get('id')] = list_task

    with open('todo_all_employees.json', mode='w') as jsonfile:
        json.dump(all_todos, jsonfile)
