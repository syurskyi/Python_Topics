_______ pytz

MEETING_HOURS r..(6, 23)  # meet from 6 - 22 max
TIMEZONES s..(pytz.all_timezones)


___ within_schedule(utc, *timezones
    """Receive a utc datetime and one or more timezones and check if
       they are all within schedule (MEETING_HOURS)"""
    __ n.. a..(tz __ TIMEZONES ___ tz __ timezones
        r.. V...('Time zone name error')
    utc pytz.utc.localize(utc)
    r.. a..(utc.astimezone(pytz.timezone(tz.hour __ MEETING_HOURS ___ tz __ timezones)
