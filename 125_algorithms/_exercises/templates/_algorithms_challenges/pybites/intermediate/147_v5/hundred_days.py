____ datetime _______ date

____ dateutil.relativedelta _______ relativedelta

TODAY = date(year=2018, month=11, day=29)
FRIDAY = 4


___ _get_weekdays(start_date):
    day = relativedelta(days=+1)
    current = start_date
    ___ x __ r..(100):
        yield current
        current += day * (3 __ current.weekday() __ FRIDAY ____ 1)


___ get_hundred_weekdays(start_date=TODAY):
    """Return a list of hundred date objects starting from
       start_date up till 100 weekdays later, so +100 days
       skipping Saturdays and Sundays"""
    r.. [current ___ current __ _get_weekdays(start_date)]
