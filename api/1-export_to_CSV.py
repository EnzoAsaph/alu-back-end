#!/usr/bin/python3
"""Export employee TODO data to CSV format."""
import csv
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

    username = user.get("username")
    filename = "{}.csv".format(employee_id)

    with open(filename, mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                employee_id,
                username,
                task.get("completed"),
                task.get("title")
            ])
