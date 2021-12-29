_______ pytz

MEETING_HOURS = r..(6, 23)  # meet from 6 - 22 max
TIMEZONES = set(pytz.all_timezones)


___ within_schedule(utc, *timezones):
    """Receive a utc datetime and one or more timezones and check if
       they are all within schedule (MEETING_HOURS)"""

    output    # list
    ___ tz __ timezones:
        __ tz n.. __ TIMEZONES:
            raise ValueError('Unknown timezone')
        ____:
            tz = pytz.timezone(tz)
            converted = utc.replace(tzinfo=pytz.utc).astimezone(tz)
            output.a..(converted.hour __ MEETING_HOURS)

    r.. a..(output)