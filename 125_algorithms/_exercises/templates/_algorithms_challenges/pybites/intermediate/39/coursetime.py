____ d__ _______ d__, t..
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
    w__ o.. COURSE_TIMES) __ file:
        course_timestamps    # list
        file_lines = file.r..
        ___ line __ file_lines:
            ts = __.f..(r"(\d{1,2}?:\d{1,2})", line)
            __ ts:
                course_timestamps.a..(ts[0])

        r.. course_timestamps


___ calc_total_course_duration(timestamps
    """Takes timestamps list as returned by get_all_timestamps
       and calculates the total duration as HH:MM:SS"""
    dt_conversion = [d__.strptime(ts, '%M:%S') ___ ts __ timestamps]
    baseline = d__(1900, 1, 1, 0, 0, 0)
    ___ course_dt __ dt_conversion:
        baseline = baseline + t..(minutes=course_dt.minute, seconds=course_dt.second)

    r.. baseline.s..('%-H:%M:%S')


#if __name__ == "__main__":
    #print(get_all_timestamps())
    #print(calc_total_course_duration(get_all_timestamps()))