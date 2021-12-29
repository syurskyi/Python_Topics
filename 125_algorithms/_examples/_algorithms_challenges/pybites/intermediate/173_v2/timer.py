from datetime import datetime, timedelta
import re

NOW = datetime(year=2019, month=2, day=6,
               hour=22, minute=0, second=0)


def add_todo(delay_time: str, task: str,
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


    values = delay_time.split()

    days = seconds = minutes = hours = 0 
    for value in values:
        v = int(value) if value[-1].isdigit() else int(value[:-1])
        if value[-1].isdigit() or value[-1] == 's':
            seconds = v
        elif value[-1] == 'd':
            days = v
        elif value[-1] == 'h':
            hours = v
        elif value[-1] == 'm':
            minutes = v 

    
    time = start_time + timedelta(hours=hours,seconds=seconds,minutes=minutes,days=days)


    return f"{task} @ {time.strftime('%Y-%m-%d %H:%M:%S')}"



    

















