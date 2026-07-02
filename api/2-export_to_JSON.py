#!/usr/bin/python3
"""
Export employee TODO data to JSON format
from https://jsonplaceholder.typicode.com
"""
import json
import requests
import sys


def main():
    """Main function to export employee TODO data to JSON."""
    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"

    user_resp = requests.get("{}/users/{}".format(base_url, employee_id))
    user = user_resp.json()
    user_id = user.get("id")
    username = user.get("username")

    todos_resp = requests.get(
        "{}/todos".format(base_url), params={"userId": employee_id})
    todos = todos_resp.json()

    tasks = []
    for task in todos:
        tasks.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    filename = "{}.json".format(user_id)
    data = {str(user_id): tasks}

    with open(filename, mode="w", encoding="utf-8") as jsonfile:
        json.dump(data, jsonfile)


if __name__ == "__main__":
    main()
