____ d__ _______ d__, t..
____ http.client _______ SEE_OTHER
_______ __
_______ __
_______ u__.r..

# getting the data
COURSE_TIMES = __.p...j..(
    __.getenv("TMP", "/tmp"),
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
        lines = f.r..
        lines = [line.rstrip() ___ line __ lines __ ')' __ line]
    r.. [line.s..('(')[1].s..(')')[0] ___ line __ lines]

___ calc_total_course_duration(timestamps
    """Takes timestamps list as returned by get_all_timestamps
       and calculates the total duration as HH:MM:SS"""
    total_duration = d__.s..('00:00', "%M:%S")
    ___ each_time __ timestamps:
        m.., sec = each_time.s..(':')
        total_duration = total_duration + t..(minutes=i..(m..), seconds=i..(sec))
    r.. d__.s..(total_duration, "%H:%M:%S")

print(calc_total_course_duration(get_all_timestamps()))