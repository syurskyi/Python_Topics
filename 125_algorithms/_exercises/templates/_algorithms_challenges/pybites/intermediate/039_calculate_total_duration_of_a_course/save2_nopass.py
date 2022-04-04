____ d__ _______ d__, t..
_______ __
_______ __
_______ u__.r..

# getting the data
COURSE_TIMES = __.p...j..(
    __.g..("TMP", "/tmp"),
    'course_timings'
)
u__.r...u..(
    'https://bites-data.s3.us-east-2.amazonaws.com/course_timings',
    COURSE_TIMES
)


___ get_all_timestamps
    """Read in the COURSE_TIMES and extract all MM:SS timestamps.
       Here is a snippet of the input file:

       Start  What is Practical JavaScript? (3:47)
       Start  The voice in your ear (4:41)
       Start  Is this course right for you? (1:21)
       ...

        Return a list of MM:SS timestamps
    """
    w__ o.. COURSE_TIMES) __ f:
        file = f.r..

    r = __.c..(r'\(\d+:\d+\)')

    l    # list
    ___ t __ file:
        t = __.s..(r, t)
        __ t != N..
            t = t.group()
            l.a..(__.sub(r'[\(\)]','', t

    r.. l


___ calc_total_course_duration(timestamps
    """Takes timestamps list as returned by get_all_timestamps
       and calculates the total duration as HH:MM:SS"""
    l = [d__.s..(date, '%M:%S') ___ date __ timestamps]
    
    deltas = [t..(seconds=t.second, minutes=t.minute)
              ___ t __ l]

    r.. s..(deltas, t..