import pytz
from datetime import datetime


MEETING_HOURS = range(6, 23)  # meet from 6 - 22 max
TIMEZONES = set(pytz.all_timezones)


def within_schedule(utc, *timezones):
    """Receive a utc datetime and one or more timezones and check if
       they are all within schedule (MEETING_HOURS)"""
    utc = pytz.utc.localize(utc)
    for timezone in timezones:
        if timezone not in TIMEZONES:
            raise ValueError
        city_local_time = utc.astimezone(pytz.timezone(timezone))
        if city_local_time.hour not in MEETING_HOURS:
            return False
    return True


dt = datetime(2018, 4, 18, 12, 28)
timezones = ['Europe/Madrid', 'Australia/Sydney', 'America/Chicago']

print(within_schedule(dt, *timezones))