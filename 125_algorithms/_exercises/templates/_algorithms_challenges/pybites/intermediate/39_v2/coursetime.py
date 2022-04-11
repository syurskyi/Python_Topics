____ d__ _______ d__, t..
_______ __
_______ __
_______ u__.r..

# getting the data
COURSE_TIMES = __.p...j..(
    __.g.. TMP  /tmp,
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

    course_times    # list
    w__ o.. COURSE_TIMES _ __ f:
        ___ line __ f:
            result = __.s..(r'\((\d+:\d+)\)',line)
            __ result:
                course_times.a..(result.group(1

    r.. course_times

___ calc_total_course_duration(timestamps
    """Takes timestamps list as returned by get_all_timestamps
       and calculates the total duration as HH:MM:SS"""
    
    time_elapsed = t..()
    ___ timestamp __ timestamps:
        minutes,seconds = timestamp.s..(':')
        minutes = i..(minutes)
        seconds = i..(seconds)
        time_elapsed += t..(minutes=minutes,seconds=seconds)

    r.. s..(time_elapsed)








