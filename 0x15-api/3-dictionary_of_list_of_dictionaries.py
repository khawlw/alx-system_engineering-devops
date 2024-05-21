#!/usr/bin/python3
"""Gather data from an API"""
import json
from urllib.request import urlopen

if __name__ == '__main__':
    url = f'https://jsonplaceholder.typicode.com/users'
    with urlopen(url) as res:
        body = res.read().decode('UTF-8')
        users = json.loads(body)

    my_dict = {}
    for user in users:
        url = f'https://jsonplaceholder.typicode.com/todos?userId={user["id"]}'
        my_list = []
        with urlopen(url) as res:
            body = res.read().decode('UTF-8')
            data = json.loads(body)
            for task in data:
                my_list.append({
                    "username": user['username'],
                    "task": task['title'],
                    "completed": task['completed']
                })
        my_dict[str(user['id'])] = my_list

    output_dict = json.dumps(my_dict, indent=4)
    with open('todo_all_employees.json', 'w') as f:
        f.write(output_dict)
