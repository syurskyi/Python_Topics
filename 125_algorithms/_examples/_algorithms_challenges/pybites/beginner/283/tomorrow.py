import datetime as dt
def tomorrow(today=None):
    # Your code goes here

    if today is None:
        today = dt.date.today()

    return today + dt.timedelta(days=1)

