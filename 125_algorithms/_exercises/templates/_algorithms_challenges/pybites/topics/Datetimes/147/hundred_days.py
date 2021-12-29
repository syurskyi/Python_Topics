____ datetime _______ date

#import dateutil
____ dateutil.rrule _______ *


TODAY = date(year=2018, month=11, day=29)


___ get_hundred_weekdays(start_date=TODAY):
    """Return a list of hundred date objects starting from
       start_date up till 100 weekdays later, so +100 days
       skipping Saturdays and Sundays"""
    pb_list = l..(rrule(DAILY, count=100, byweekday=(MO, TU, WE, TH, FR),dtstart=start_date))
    r.. [pb.date() ___ pb __ pb_list]

dt_list = get_hundred_weekdays()
print(type(dt_list))
print(type(dt_list[0]))