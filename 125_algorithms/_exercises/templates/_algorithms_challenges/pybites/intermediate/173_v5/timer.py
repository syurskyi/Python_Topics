____ d__ _______ d__, t..

NOW d__ y.._2019,  m.._2,  d.._6,
               hour=22, minute=0, second=0)


___ add_todo(delay_time: s.., task: s..,
             start_time: d__ NOW) __ s..:
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
    delay delay_time.s..
    td start_time
    ___ dl __ delay:
        __ dl[-1] __ 'd':
            td += t..(d.._i..(dl[:-1]
        ____ dl[-1] __ 'h':
            td += t..(hours=i..(dl[:-1]
        ____ dl[-1] __ 'm':
            td += t..(minutes=i..(dl[:-1]
        ____ dl[-1] __ 's':
            td += t..(s.._i..(dl[:-1]
        ____
            td += t..(s.._i..(dl
    r.. _* task} @ {td.s..("_Y-%m-_d _H|_M:_S")}'
