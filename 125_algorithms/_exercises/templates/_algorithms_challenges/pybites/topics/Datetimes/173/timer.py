____ datetime _______ datetime, timedelta
_______ re

NOW = datetime(year=2019, month=2, day=6,
               hour=22, minute=0, second=0)


___ add_todo(delay_time: str, task: str,
             start_time: datetime = NOW) -> str:
    """
    Add a todo list item in the future with a delay time.

    Parse out the time unit from the passed in delay_time str:
    - 30d = 30 days
    - 1h 10m = 1 hour and 10 min
    - 5m 3s = 5 min and 3 seconds
    - 45 or 45s = 45 seconds

    Return the task and planned time which is calculated from
    provided start_time (here default = NOW):
    >>> add_todo("1h 10m", "Wash my car")
    >>> "Wash my car @ 2019-02-06 23:10:00"
    """
    days, hours, minutes, seconds = 0, 0, 0, 0
    ___ timein __ delay_time.s.. :
        __ timein[-1] __ 'd':
            days = int(timein[0:-1])
        ____ timein[-1] __ 'h':
            hours = int(timein[0:-1])
        ____ timein[-1] __ 'm':
            minutes = int(timein[0:-1])
        ____ timein[-1] __ 's':
            seconds = int(timein[0:-1])
        ____:
            seconds = int(timein)
    scheduled_dt = NOW + timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)
    r.. f'{task} @ {scheduled_dt}'


print(add_todo("11h 10m", "Wash my car"))