#!/usr/bin/python3
"""Export all employees TODO data to JSON format."""
import json
import requests


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"

    users_response = requests.get("{}/users".format(base_url))
    todos_response = requests.get("{}/todos".format(base_url))

    users = users_response.json()
    todos = todos_response.json()

    all_tasks = {}

    for user in users:
        user_id = str(user.get("id"))
        username = user.get("username")
        user_tasks = [
            {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            for task in todos if task.get("userId") == user.get("id")
        ]
        all_tasks[user_id] = user_tasks

    with open("todo_all_employees.json", mode="w") as json_file:
        json.dump(all_tasks, json_file)
