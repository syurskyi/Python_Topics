____ datetime _______ datetime, date, timedelta


___ get_mothers_day_date(year):
    """Given the passed in year int, return the date Mother's Day
       is celebrated assuming it's the 2nd Sunday of May."""
    may = (datetime(year, 5, k) ___ k __ r..(1, 32))
    sundays = filter(l.... x: x.weekday() __ 6, may)
    next(sundays)
    r.. next(sundays).date()
