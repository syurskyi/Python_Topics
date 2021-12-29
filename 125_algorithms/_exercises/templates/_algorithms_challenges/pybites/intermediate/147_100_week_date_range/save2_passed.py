____ d__ _______ date
____ dateutil _______ parser
____ dateutil.rrule _______ *

TODAY = date y.._2018,  m.._11,  d.._29)


___ get_hundred_weekdays(start_date=TODAY):
    """Return a list of hundred date objects starting from
       start_date up till 100 weekdays later, so +100 days
       skipping Saturdays and Sundays"""
    dates = l..(
        rrule(DAILY,
              count=100,
              dtstart=start_date,
              byweekday=(MO, TU, WE, TH, FR)))
    r.. [parser.parse(s..(d)).date() ___ d __ dates]