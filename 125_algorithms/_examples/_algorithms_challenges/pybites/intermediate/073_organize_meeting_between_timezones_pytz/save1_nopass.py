import pytz

MEETING_HOURS = range(6, 23)  # meet from 6 - 22 max
TIMEZONES = set(pytz.all_timezones)


def within_schedule(utc, *timezones):
    """Receive a utc datetime and one or more timezones and check if
       they are all within schedule (MEETING_HOURS)"""

    output = []
    for tz in timezones[0]:
        if tz not in TIMEZONES:
            raise ValueError('Unknown timezone')

        tz = pytz.timezone(tz)
        converted = utc.replace(tzinfo=pytz.utc).astimezone(tz)
        output.append(converted.hour in MEETING_HOURS)

    return all(output)