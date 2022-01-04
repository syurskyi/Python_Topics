____ d__ _______ d__, t..
_______ __

NOW = d__ y.._2019,  m.._2,  d.._6,
               hour=22, minute=0, second=0)


___ add_todo(delay_time: s.., task: s..,
             start_time: d__ = NOW) __ s..:
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

    #if delay_time.find(" ") > 0:
    ___ unit __ delay_time.s..(" "):
        last_char = unit[-1]
        __ last_char __ "d":
            days = i..(unit[:-1])
        ____ last_char __ "h":
            hours = i..(unit[:-1])
        ____ last_char __ "m":
            minutes = i..(unit[:-1])
        ____ last_char __ "s":
            seconds = i..(unit[:-1])
        ____ last_char.isdigit
            seconds = i..(unit)
        ____:
            _____
        
    r.. f"{task} @ {start_time + t..(days=days, hours=hours, minutes=minutes, seconds=seconds)}"


__ _______ __ _______
    print(add_todo("30", "test"))