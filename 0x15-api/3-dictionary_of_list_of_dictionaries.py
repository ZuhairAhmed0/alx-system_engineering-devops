#!/usr/bin/python3
"""Python script to export data in the JSON format."""
import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()
    todos requests.get(url + "todos", params={"userId": user.get("id")}).json()
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({user.get("id"): [{
                 "task": todo.get("title"),
                 "completed": todo.get("completed"),
                 "username": user.get("username")
                 } for todo in todos]
                 for user in users}, jsonfile)
