import pytz
from dateutil import tz

MEETING_HOURS = range(6, 23)  # meet from 6 - 22 max
TIMEZONES = set(pytz.all_timezones)


def within_schedule(utc, *timezones):
    """Receive a utc datetime and one or more timezones and check if
       they are all within schedule (MEETING_HOURS)"""
    utc = utc.replace(tzinfo=tz.UTC)

    for timezone in timezones:
        timezone = tz.gettz(timezone)
        if not timezone:
            raise ValueError
        date = utc.astimezone(timezone)

        if not date.hour in MEETING_HOURS:
            return False

    return True





    
