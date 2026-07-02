#!/usr/bin/python3
"""Gather data from an API and display employee TODO list progress."""
import json
import ssl
import sys
import urllib.request

ssl._create_default_https_context = ssl._create_unverified_context

if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"

    with urllib.request.urlopen(
            "{}/users/{}".format(base_url, employee_id)) as r:
        user = json.loads(r.read().decode('utf-8'))

    with urllib.request.urlopen(
            "{}/todos?userId={}".format(base_url, employee_id)) as r:
        todos = json.loads(r.read().decode('utf-8'))

    employee_name = user.get("name")
    done_tasks = [task for task in todos if task.get("completed")]
    total_tasks = len(todos)
    number_of_done_tasks = len(done_tasks)

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, number_of_done_tasks, total_tasks
    ))

    for task in done_tasks:
        print("\t {}".format(task.get("title")))
