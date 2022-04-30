____ d__ _______ d__, t..
_______ __

NOW d__ y.._2019,  m.._2,  d.._6,
               h.._22, m.._0 s.._0


___ add_todo delay_time s.. task s..
             start_time d__ N.. __ s..
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
    days, hours, minutes, seconds 0, 0, 0, 0
    ___ timein __ ?.s.. :
        __ timein[-1] __ 'd':
            days i..(timein[0:-1])
        ____ timein[-1] __ 'h':
            hours i..(timein[0:-1])
        ____ timein[-1] __ 'm':
            minutes i..(timein[0:-1])
        ____ timein[-1] __ 's':
            seconds i..(timein[0:-1])
        ____
            seconds i..(timein)
    scheduled_dt NOW + t..(d.._days, h.._hours, m.._? s.._?
    r.. _* task} @ {scheduled_dt}'


print(add_todo("11h 10m", "Wash my car"