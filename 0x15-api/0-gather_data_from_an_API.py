#!/usr/bin/python3
"""Gather data from an API"""
import json
from sys import argv
from urllib.request import urlopen

if __name__ == '__main__':
    userId = argv[1]

    url = f'https://jsonplaceholder.typicode.com/users?id={userId}'
    with urlopen(url) as res:
        body = res.read().decode('UTF-8')
    data = json.loads(body)
    name = data[0]['name']

    url = f'https://jsonplaceholder.typicode.com/todos?userId={userId}'
    with urlopen(url) as res:
        body = res.read().decode('UTF-8')
    data = json.loads(body)

    n = len(data)
    count = 0
    for task in data:
        if task['completed'] is True:
            count += 1

    print(f'Employee {name} is done with tasks({count}/{n}):')

    for task in data:
        print('\t', task['title'])
