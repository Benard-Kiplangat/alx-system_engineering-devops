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
    new_dict1 = {}

    for j in data2:

        row = []
        for i in data:

            new_dict2 = {}

            if j.get('id') == i['userId']:

                new_dict2['username'] = j.get('username')
                new_dict2['task'] = i.get('title')
                new_dict2['completed'] = i.get('completed')
                row.append(new_dict2)

        new_dict1[j.get('id')] = row

    with open("todo_all_employees.json",  "w") as f:

        json_obj = json.dumps(new_dict1)
        f.write(json_obj)
