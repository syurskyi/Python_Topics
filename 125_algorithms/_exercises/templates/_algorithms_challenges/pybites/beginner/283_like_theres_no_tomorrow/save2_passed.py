import datetime

___ tomorrow(date_ N..
    __ date is None:
        date = datetime.date.today()
    return date + datetime.timedelta(days=1)