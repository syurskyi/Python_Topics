_______ p__
____ d__ _______ d__


MEETING_HOURS r..(6, 23)  # meet from 6 - 22 max
TIMEZONES s.. p__.a..


___ within_schedule(utc $timezones
    """Receive a utc datetime and one or more timezones and check if
       they are all within schedule (MEETING_HOURS)"""
    utc p__.utc.l.. u..
    ___ timezone __ ?
        __ timezone n.. __ T..
            r.. V...
        city_local_time utc.a..(p__.t..(timezone
        __ city_local_time.hour n.. __ MEETING_HOURS:
            r.. F..
    r.. T..


dt d__(2018, 4, 18, 12, 28)
timezones =  'Europe/Madrid', 'Australia/Sydney', 'America/Chicago'

print(within_schedule(dt $timezones