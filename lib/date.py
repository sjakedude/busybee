from datetime import datetime


def validate_date(date):
    month = int(date[0:2])
    day = int(date[3:5])
    year = int(date[6:10])
    if month < 0 or month > 12:
        raise Exception
    if day < 0 or day > 31:
        raise Exception
    if year < 1000 or year > 3000:
        raise Exception


class Date:
    def __init__(self, date):
        validate_date(date)
        self.date = date
        self.tasks = []

    def add_task(self, task_id):
        self.tasks.append(task_id)
