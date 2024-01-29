#!/usr/bin/python3

"""
A script that returns a given employees information
about his/her TODO list progress
"""

from requests import get
from sys import argv
import csv

if __name__ == "__main__":
    response = get('https://jsonplaceholder.typicode.com/todos/')
    data = response.json()
    response2 = get('https://jsonplaceholder.typicode.com/users')
    data2 = response2.json()
    row = []

    for i in data2:
        if i.get('id') == int(argv[1]):
            employee = i.get('username')

    with open(argv[1] + '.csv', 'w', newline='') as file:
        writ = csv.writer(file, quoting=csv.QUOTE_ALL)

        for i in data:

            row = []
            if i.get('userId') == int(argv[1]):
                row.append(i.get('userId'))
                row.append(employee)
                row.append(i.get('completed'))
                row.append(i.get('title'))

                writ.writerow(row)
