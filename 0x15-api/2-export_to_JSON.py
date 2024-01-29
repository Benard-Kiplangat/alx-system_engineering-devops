#!/usr/bin/python3

"""
A script that returns a given employees information
about his/her TODO list progress
"""

from requests import get
from sys import argv
import json

if __name__ == "__main__":
    response = get('https://jsonplaceholder.typicode.com/todos/')
    data = response.json()
    response2 = get('https://jsonplaceholder.typicode.com/users')
    data2 = response2.json()
    row = []
    new_dict = {}

    for i in data2:
        if i.get('id') == int(argv[1]):
            u_name = i.get('username')
            id_no = i.get('id')


    for i in data:

        new_dict = {}

        if i.get('userId') == int(argv[1]):
            new_dict['username'] = u_name
            new_dict['task'] = i.get('title')
            new_dict['completed'] = i.get('completed')
            row.append(new_dict)

    final_dict = {}
    final_dict[id_no] = row
    json_obj = json.dumps(final_dict)


    with open(argv[1] + ".json",  "w") as f:
        f.write(json_obj)
