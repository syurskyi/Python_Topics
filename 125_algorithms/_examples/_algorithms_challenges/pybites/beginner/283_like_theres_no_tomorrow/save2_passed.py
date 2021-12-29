import datetime

def tomorrow(date=None):
    if date is None:
        date = datetime.date.today()
    return date + datetime.timedelta(days=1)