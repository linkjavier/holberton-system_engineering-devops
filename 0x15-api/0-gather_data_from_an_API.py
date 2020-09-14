#!/usr/bin/python3
""" """

import requests
from sys import argv


if __name__ == "__main__":

    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                       .format(argv[1]))
    name = user.json().get('name')
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    alltask = 0
    done = 0

    for task in todos.json():
        if task.get('userId') == int(argv[1]):
            alltask += 1
            if task.get('completed'):
                done += 1
    print('Employee {} is done with tasks({}/{})'
          .format(name, done, alltask))

    print('\n'.join(['   ' + task.get('title') for task in todos.json()
                     if task.get('userId') == int(argv[1])
                     and task.get('completed')]))
