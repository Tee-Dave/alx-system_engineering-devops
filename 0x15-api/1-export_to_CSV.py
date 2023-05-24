#!/usr/bin/python3
"""
    Calls to data from the jsonplaceholder website parsed to csv formats
    from task 0, extend your Python script to export data in the CSV format
"""
if __name__ == "__main__":
    """
        extend your Python script i task 0 to export data in the CSV format
    """

    import csv
    import requests
    import sys

    EMPLOYEE_ID = sys.argv[1]

    link = "https://jsonplaceholder.typicode.com/users"
    userResponse = requests.get(f"{link}/{EMPLOYEE_ID}")
    EMPLOYEE_NAME = userResponse.json().get("name")
    fileName = "{}.csv".format(EMPLOYEE_ID)

    todoList = requests.get(f"{link}/{EMPLOYEE_ID}/todos").json()
    with open(fileName, "w", newline="") as fd:
        pen = csv.writer(
                fd,
                delimiter=',',
                quotechar='"',
                quoting=csv.QUOTE_ALL
            )

        for task in todoList:
            line = [
                    EMPLOYEE_ID,
                    EMPLOYEE_NAME,
                    task.get('completed'),
                    task.get('title')
                ]

            pen.writerow(line)
