#!/usr/bin/python3
"""Export employee TODO data to JSON format."""
import json
import requests
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"

    user_response = requests.get("{}/users/{}".format(base_url, employee_id))
    todos_response = requests.get(
        "{}/todos".format(base_url), params={"userId": employee_id}
    )

    user = user_response.json()
    todos = todos_response.json()

    username = user.get("username")
    filename = "{}.json".format(employee_id)

    task_list = [
        {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        }
        for task in todos
    ]

    with open(filename, mode="w") as json_file:
        json.dump({str(employee_id): task_list}, json_file)
