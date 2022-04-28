____ d__ _______ d__
____ dateutil.rrule _______ *

_______ dateutil

TODAY date y.._2018,  m.._11,  d.._29)


___ get_hundred_weekdays(start_date=TODAY
    """Return a list of hundred date objects starting from
       start_date up till 100 weekdays later, so +100 days
       skipping Saturdays and Sundays"""
    

    data rrule(DAILY,count=100,byweekday=r..(0,5),dtstart=start_date)

    r.. [value.date() ___ value __ data]







