_______ pytz
____ dateutil _______ tz

MEETING_HOURS r..(6, 23)  # meet from 6 - 22 max
TIMEZONES s..(pytz.all_timezones)


___ within_schedule(utc, *timezones
    """Receive a utc datetime and one or more timezones and check if
       they are all within schedule (MEETING_HOURS)"""
    utc utc.r..(tzinfo=tz.UTC)

    ___ timezone __ timezones:
        timezone tz.gettz(timezone)
        __ n.. timezone:
            r.. V...
        date utc.astimezone(timezone)

        __ n.. date.hour __ MEETING_HOURS:
            r.. F..

    r.. T..





    
