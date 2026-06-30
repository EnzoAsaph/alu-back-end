#!/usr/bin/python3
"""Export all employees TODO data to JSON format."""
import json
import ssl
import urllib.request


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    with urllib.request.urlopen(
            "{}/users".format(base_url), context=ctx) as r:
        users = json.loads(r.read().decode('utf-8'))

    with urllib.request.urlopen(
            "{}/todos".format(base_url), context=ctx) as r:
        todos = json.loads(r.read().decode('utf-8'))

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
