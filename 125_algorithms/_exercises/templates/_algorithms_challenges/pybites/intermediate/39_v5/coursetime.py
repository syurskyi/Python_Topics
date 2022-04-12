____ d__ _______ d__, t..
_______ __
_______ __
_______ u__.r..

# getting the data
COURSE_TIMES __.p...j..('/tmp', 'course_timings')
u__.r...u..('http://bit.ly/2Eb0iQF', COURSE_TIMES)


___ get_all_timestamps
    """Read in the COURSE_TIMES and extract all MM:SS timestamps.
       Here is a snippet of the input file:

       Start  What is Practical JavaScript? (3:47)
       Start  The voice in your ear (4:41)
       Start  Is this course right for you? (1:21)
       ...

        Return a list of MM:SS timestamps
    """
    result    # list
    w__ o.. COURSE_TIMES) __ ct:
        ___ line __ ct.r..
            times __.f.. _ \((\d\d?:\d\d)\)', line)
            __ l..(times) > 0
                result.a..(times 0
    r.. result


___ calc_total_course_duration(timestamps
    """Takes timestamps list as returned by get_all_timestamps
       and calculates the total duration as HH:MM:SS"""
    total_time s..(t..(minutes=xt.minute, seconds=xt.second).total_seconds()
                     ___ t __ timestamps
                     ___ xt __ [d__.s..(t, '_M:_S')])
    r.. s..(t..(seconds=total_time
