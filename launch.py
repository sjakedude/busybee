import os
from lib.date import Date
from lib.task import Task

def display_tasks(date):
    index = 1
    for task in date.tasks:
        print(str(index) + ". " + task.name)

def main():
    print("Here we go...")
    date = input("Enter date: (MM/DD/YYYY) ")
    date = Date(date)
    display_tasks(date)
    answer = input("Add task? (Y or N) ")
    if answer == "Y":
        task = input("Enter task: ")
        task = Task(task)
        date.add_task(task)
    display_tasks(date)

    
    

main()
