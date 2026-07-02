#!/usr/bin/python3
"""
Export employee TODO data to CSV format
from https://jsonplaceholder.typicode.com
"""
import csv
import requests
import sys


def main():
    """Main function to export employee TODO data to CSV."""
    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"

    user_resp = requests.get("{}/users/{}".format(base_url, employee_id))
    user = user_resp.json()
    user_id = user.get("id")
    username = user.get("username")

    todos_resp = requests.get(
        "{}/todos".format(base_url), params={"userId": employee_id})
    todos = todos_resp.json()

    filename = "{}.csv".format(user_id)
    with open(filename, mode="w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                user_id,
                username,
                task.get("completed"),
                task.get("title")
            ])


if __name__ == "__main__":
    main()
