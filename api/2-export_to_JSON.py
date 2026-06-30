#!/usr/bin/python3
"""Export employee TODO data to JSON format."""
import json
import ssl
import sys
import urllib.request


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    with urllib.request.urlopen(
            "{}/users/{}".format(base_url, employee_id),
            context=ctx) as r:
        user = json.loads(r.read().decode('utf-8'))

    with urllib.request.urlopen(
            "{}/todos?userId={}".format(base_url, employee_id),
            context=ctx) as r:
        todos = json.loads(r.read().decode('utf-8'))

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
