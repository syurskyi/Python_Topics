from datetime import date
from dateutil import parser
from dateutil.rrule import *

TODAY = date(year=2018, month=11, day=29)


def get_hundred_weekdays(start_date=TODAY):
    """Return a list of hundred date objects starting from
       start_date up till 100 weekdays later, so +100 days
       skipping Saturdays and Sundays"""
    dates = list(
        rrule(DAILY,
              count=100,
              dtstart=start_date,
              byweekday=(MO, TU, WE, TH, FR)))
    return [parser.parse(str(d)).date() for d in dates]