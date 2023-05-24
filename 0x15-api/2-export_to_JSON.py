#!/usr/bin/python3
"""
    Calls to data from the jsonplaceholder website parsed to json formats
    from task 0, extend your Python script to export data in the JSON format.
"""
if __name__ == "__main__":
    """
        Calls to data from the jsonplaceholder website
        parsed to json formats from task 0, extend your
        Python script to export data in the JSON format.
    """
    import json
    import requests
    import sys

    EMPLOYEE_ID = sys.argv[1]

    link = "https://jsonplaceholder.typicode.com/users"
    userResponse = requests.get(f"{link}/{EMPLOYEE_ID}")
    EMPLOYEE_NAME = userResponse.json().get("name")
    fileName = "{}.json".format(EMPLOYEE_ID)

    todoList = requests.get(f"{link}/{EMPLOYEE_ID}/todos").json()

    tasks = []
    for task in todoList:
        taskDict = {}
        taskDict["task"] = task.get('title')
        taskDict["completed"] = task.get('completed')
        taskDict["username"] = EMPLOYEE_NAME
        tasks.append(taskDict)

    todoDict = {EMPLOYEE_ID: tasks}

    with open(fileName, "w", newline="") as fd:
        json.dump(todoDict, fd)
