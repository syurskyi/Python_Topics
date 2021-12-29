import datetime as dt
___ tomorrow(today_ N..
    # Your code goes here

    __ today is None:
        today = dt.date.today()

    return today + dt.timedelta(days=1)

