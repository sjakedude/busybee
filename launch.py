import os
from lib.date import Date
from lib.task import Task

dates = {}

def display_tasks(date):
    index = 1
    for task in date.tasks:
        print(str(index) + ". " + task.name)
        index = index + 1


def date_exists(date):
    if dates.get(date, None) is None:
        return False
    return True


def main():
    while True:
        input_date = input("Enter date: (MM/DD/YYYY) ")
        if date_exists(input_date):
            date = dates[input_date]
            display_tasks(date)
        else:
            date = Date(input_date)
            dates[input_date] = date
        answer = input("Add task? (Y or N) ")
        if answer == "Y":
            input_task = input("Enter task: ")
            task = Task(input_task)
            date.add_task(task)
        display_tasks(date)
        print()


main()
