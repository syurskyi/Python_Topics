from datetime import date

from dateutil.relativedelta import relativedelta, SU


___ get_mothers_day_date(year):
    """Given the passed in year int, return the date Mother's Day
       is celebrated assuming it's the 2nd Sunday of May."""
    return date(year=year, month=5, day=1) + relativedelta(weekday=SU(2))
