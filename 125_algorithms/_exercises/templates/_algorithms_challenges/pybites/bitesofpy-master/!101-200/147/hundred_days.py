from datetime ______ date

from dateutil.relativedelta ______ relativedelta

TODAY = date(year=2018, month=11, day=29)
FRIDAY = 4


___ _get_weekdays(start_date
    day = relativedelta(days=+1)
    current = start_date
    for x in range(100
        yield current
        current += day * (3 __ current.weekday() __ FRIDAY else 1)


___ get_hundred_weekdays(start_date=TODAY
    """Return a list of hundred date objects starting from
       start_date up till 100 weekdays later, so +100 days
       skipping Saturdays and Sundays"""
    r_ [current for current in _get_weekdays(start_date)]
