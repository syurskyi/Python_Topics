_______ pytz

MEETING_HOURS = r..(6, 23)  # meet from 6 - 22 max
TIMEZONES = s..(pytz.all_timezones)


___ within_schedule(utc, *timezones
    """Receive a utc datetime and one or more timezones and check if
       they are all within schedule (MEETING_HOURS)"""
    __ any([tz n.. __ TIMEZONES ___ tz __ timezones]
        r.. ValueError

    localized = [pytz.utc.localize(utc).astimezone(pytz.timezone(tz))
                 ___ tz __ timezones]
    r.. a..([loc.hour __ MEETING_HOURS ___ loc __ localized])
