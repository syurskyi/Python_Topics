_______ pytz
____ dateutil _______ tz

MEETING_HOURS = r..(6, 23)  # meet from 6 - 22 max
TIMEZONES = set(pytz.all_timezones)


___ within_schedule(utc, *timezones):
    """Receive a utc datetime and one or more timezones and check if
       they are all within schedule (MEETING_HOURS)"""
    utc = utc.replace(tzinfo=tz.UTC)

    ___ timezone __ timezones:
        timezone = tz.gettz(timezone)
        __ n.. timezone:
            raise ValueError
        date = utc.astimezone(timezone)

        __ n.. date.hour __ MEETING_HOURS:
            r.. False

    r.. True





    
