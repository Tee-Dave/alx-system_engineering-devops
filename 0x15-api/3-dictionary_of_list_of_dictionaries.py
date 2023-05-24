#!/usr/bin/python3
"""
    Calls all data from the jsonplaceholder website parsed to json formats
    Using what you did in the task #0, extend your Python
    script to export data in the JSON format.
"""
if __name__ == "__main__":
    """
        Calls all data from the jsonplaceholder website parsed to json
        formats Using what you did in the task #0, extend your Python
        script to export data in the JSON format.
    """
    import json
    import requests
    import sys

    link = "https://jsonplaceholder.typicode.com"
    fileName = "todo_all_employees.json"

    employeeList = requests.get(f"{link}/users").json()
    allTodoList = requests.get(f"{link}/todos").json()

    todoDict = {}

    for user in employeeList:
        tasks = []
        userId = user.get('id')
        for task in allTodoList:
            if task.get("userId") == userId:
                taskDict = {}
                taskDict["username"] = user.get('username')
                taskDict["task"] = task.get('title')
                taskDict["completed"] = task.get('completed')
                tasks.append(taskDict)
        todoDict[userId] = tasks

    with open(fileName, "w", newline="") as fd:
        json.dump(todoDict, fd)
