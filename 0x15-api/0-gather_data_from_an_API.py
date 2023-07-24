#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""


import requests
import sys

url = 'https://jsonplaceholder.typicode.com'
empId = sys.argv[1]

response = requests.get('{}/todos?userId={}'.format(url, empId))

todos = response.json()
num_completed_task = sum(1 for todo in todos if todo["completed"])
num_total_task = len(todos)

response = requests.get('{}/users/{}'.format(url, empId))
empName = response.json()["name"]

print("Employee {} is done with tasks({}/{}):".format(empName, num_completed_task, num_total_task))
for todo in todos:
    if todo["completed"]:
        print("\t{}".format(todo["title"]))

