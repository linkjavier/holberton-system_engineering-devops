#!/usr/bin/python3
""" Script to export data in the CSV format.
"""

import requests
from sys import argv
import csv


if __name__ == "__main__":

    filename = argv[1] + '.csv'
    with open(filename, mode='w') as csvfile:

        user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                            .format(argv[1]))
        name = user.json().get('name')
        todos = requests.get('https://jsonplaceholder.typicode.com/todos')

        writer = csv.writer(csvfile,
                            delimiter=',',
                            quotechar='"',
                            quoting=csv.QUOTE_ALL)
        for task in todos.json():
            writer.writerow([argv[1], name, task.get('completed'),
                             task.get('title')])
