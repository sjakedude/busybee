import os
from lib.date import Date
from lib.task import Task


def display_tasks(date):
    index = 1
    for task in date.tasks:
        print(str(index) + ". " + task.name)


def main():
    while True:
        input_date = input("Enter date: (MM/DD/YYYY) ")
        print("u entered")
        print(input_date)
        date = Date(input_date)
        display_tasks(date)
        answer = input("Add task? (Y or N) ")
        if answer == "Y":
            input_task = input("Enter task: ")
            task = Task(input_task)
            date.add_task(task)
        display_tasks(date)
        print()


main()
