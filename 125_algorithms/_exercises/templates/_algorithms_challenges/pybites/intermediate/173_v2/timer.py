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


    values = delay_time.s.. 

    days = seconds = minutes = hours = 0 
    ___ value __ values:
        v = i..(value) __ value[-1].i.. ____ i..(value[:-1])
        __ value[-1].i.. o. value[-1] __ 's':
            seconds = v
        ____ value[-1] __ 'd':
            days = v
        ____ value[-1] __ 'h':
            hours = v
        ____ value[-1] __ 'm':
            minutes = v 

    
    time = start_time + t..(hours=hours,seconds=seconds,minutes=minutes,d.._days)


    r.. f"{task} @ {time.s..('%Y-%m-%d %H:%M:%S')}"



    

















