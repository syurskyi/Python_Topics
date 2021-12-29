from datetime import datetime, date, timedelta


def get_mothers_day_date(year):
    """Given the passed in year int, return the date Mother's Day
       is celebrated assuming it's the 2nd Sunday of May."""
    may = (datetime(year, 5, k) for k in range(1, 32))
    sundays = filter(lambda x: x.weekday() == 6, may)
    next(sundays)
    return next(sundays).date()
