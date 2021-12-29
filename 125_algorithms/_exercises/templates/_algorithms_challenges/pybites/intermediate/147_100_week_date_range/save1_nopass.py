____ datetime _______ date
____ dateutil.rrule _______ *

TODAY = date(year=2018, month=11, day=29)


___ get_hundred_weekdays(start_date=TODAY):
    """Return a list of hundred date objects starting from
       start_date up till 100 weekdays later, so +100 days
       skipping Saturdays and Sundays"""
    r.. l..(
        rrule(DAILY,
              count=100,
              dtstart=start_date,
              byweekday=(MO,TU,WE,TH,FR)))