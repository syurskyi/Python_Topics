import pytz

MEETING_HOURS = range(6, 23)  # meet from 6 - 22 max
TIMEZONES = set(pytz.all_timezones)


___ within_schedule(utc, *timezones):
    """Receive a utc datetime and one or more timezones and check if
       they are all within schedule (MEETING_HOURS)"""
    __ any([tz not in TIMEZONES for tz in timezones]):
        raise ValueError

    localized = [pytz.utc.localize(utc).astimezone(pytz.timezone(tz))
                 for tz in timezones]
    return all([loc.hour in MEETING_HOURS for loc in localized])
