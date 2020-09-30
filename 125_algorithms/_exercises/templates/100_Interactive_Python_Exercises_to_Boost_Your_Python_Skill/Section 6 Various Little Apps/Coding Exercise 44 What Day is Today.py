import datetime


def foo(date):
    return datetime.datetime.strptime(date, "%Y-%m-%d").strftime("%A")
