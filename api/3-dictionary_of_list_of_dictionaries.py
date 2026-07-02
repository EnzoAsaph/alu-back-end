#!/usr/bin/python3
"""
Export all employees TODO data to JSON format
from https://jsonplaceholder.typicode.com
"""
import json
import requests


def main():
    """Main function to export all employees TODO data to JSON."""
    base_url = "https://jsonplaceholder.typicode.com"

    users_resp = requests.get("{}/users".format(base_url))
    users = users_resp.json()

    todos_resp = requests.get("{}/todos".format(base_url))
    todos = todos_resp.json()

    user_map = {}
    for user in users:
        user_map[user.get("id")] = user.get("username")

    all_tasks = {}
    for task in todos:
        user_id = task.get("userId")
        user_id_str = str(user_id)

        if user_id_str not in all_tasks:
            all_tasks[user_id_str] = []

        all_tasks[user_id_str].append({
            "username": user_map[user_id],
            "task": task.get("title"),
            "completed": task.get("completed")
        })

    with open("todo_all_employees.json", mode="w", encoding="utf-8") as f:
        json.dump(all_tasks, f)


if __name__ == "__main__":
    main()
