'''
Get to know pytz! pytz brings the Olson tz database into Python (docs). Let's see how many hours Bob and Julian have to
bridge in order to deliver you PyBites. It differs depending on whether it's Winter or Summer in their relative hemispheres.

Complete the what_time_lives_pybites function which receives a naive / not timezone aware datetime object:

There are two kinds of date and time objects: naive and aware: an aware object has sufficient knowledge of
applicable algorithmic and political time adjustments, such as time zone and daylight saving time information,
to locate itself relative to other aware objects. An aware object is used to represent a specific moment in time that is
not open to interpretation. - docs

First convert the passed in naive_utc_dt to a aware datetime, then convert it to AUSTRALIA and SPAIN localized
datetimes returning them in a tuple. For a bit more advanced pytz Bite try Bite 73 ...

Have fun and keep coding in Python!
'''

from pytz import timezone, utc
from datetime import datetime

AUSTRALIA = timezone('Australia/Sydney')
SPAIN = timezone('Europe/Madrid')


def what_time_lives_pybites(naive_utc_dt):
    """Receives a naive UTC datetime object and returns a two element
       tuple of Australian and Spanish (timezone aware) datetimes"""
    au = naive_utc_dt.astimezone(AUSTRALIA)
    es = naive_utc_dt.astimezone(SPAIN)
    t = (au,es)
    return t

now = datetime.now()
result = what_time_lives_pybites(now)
print(result[0])
print(result[1])

