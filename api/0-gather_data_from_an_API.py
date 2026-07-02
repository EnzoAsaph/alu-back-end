#!/usr/bin/python3
"""
Fetch and display an employee's TODO list progress
from https://jsonplaceholder.typicode.com
"""
import requests
import sys


def main():
    """Main function to gather and display employee TODO progress."""
    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"

    user_resp = requests.get("{}/users/{}".format(base_url, employee_id))
    user = user_resp.json()
    employee_name = user.get("name")

    todos_resp = requests.get(
        "{}/todos".format(base_url), params={"userId": employee_id})
    todos = todos_resp.json()

    total_tasks = len(todos)
    completed_tasks = [t for t in todos if t.get("completed") is True]
    done_tasks = len(completed_tasks)

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, done_tasks, total_tasks))

    for task in completed_tasks:
        print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    main()
