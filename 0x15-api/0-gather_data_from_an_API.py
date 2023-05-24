#!/usr/bin/python3
"""
    Using REST API, for a given employee ID, returns information about his/her
    TODO list progress. Calls to data from the jsonplaceholder website. The
    script must display on the standard output the employee TODO list progress
"""
if __name__ == "__main__":
    """ Second and N next lines display the title of completed tasks """

    import requests
    import sys

    EMPLOYEE_ID = sys.argv[1]

    link = "https://jsonplaceholder.typicode.com/users"
    user_response = requests.get(f"{link}/{EMPLOYEE_ID}")
    EMPLOYEE_NAME = user_response.json().get("name")

    todo_list = requests.get(f"{link}/{EMPLOYEE_ID}/todos").json()
    total = len(todo_list)
    completed = [
            task.get('title')
            for task in todo_list
            if task.get('completed') is True
        ]

    print("Employee {} is done with tasks({}/{})".format(
        EMPLOYEE_NAME,
        len(completed),
        total))

    for task in completed:
        print(f"\t {task}")
