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
    username = data[0]['username']

    url = f'https://jsonplaceholder.typicode.com/todos?userId={userId}'
    with urlopen(url) as res:
        body = res.read().decode('UTF-8')
    data = json.loads(body)

    my_list = []
    for task in data:
        my_list.append({
            'task': task['title'],
            'completed': task['completed'],
            'username': username
        })

    my_dict = {userId: my_list}
    json_obj = json.dumps(my_dict)
    with open(f'{userId}.json', 'w') as f:
        f.write(json_obj)
