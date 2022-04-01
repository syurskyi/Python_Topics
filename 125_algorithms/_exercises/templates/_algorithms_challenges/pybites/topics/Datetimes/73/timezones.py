_______ pytz
____ d__ _______ d__


MEETING_HOURS = r..(6, 23)  # meet from 6 - 22 max
TIMEZONES = s..(pytz.all_timezones)


___ within_schedule(utc, *timezones):
    """Receive a utc datetime and one or more timezones and check if
       they are all within schedule (MEETING_HOURS)"""
    utc = pytz.utc.localize(utc)
    ___ timezone __ timezones:
        __ timezone n.. __ TIMEZONES:
            r.. ValueError
        city_local_time = utc.astimezone(pytz.timezone(timezone))
        __ city_local_time.hour n.. __ MEETING_HOURS:
            r.. F..
    r.. T..


dt = d__(2018, 4, 18, 12, 28)
timezones = ['Europe/Madrid', 'Australia/Sydney', 'America/Chicago']

print(within_schedule(dt, *timezones))