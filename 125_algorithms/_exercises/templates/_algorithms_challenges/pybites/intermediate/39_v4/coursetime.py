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
    w__ o.. COURSE_TIMES, _ __ f:
        text = f.r..

    r.. __.f..(r'\d*:*\d*:\d{2}', text, flags=__.MULTILINE)


___ calc_total_course_duration(timestamps
    """Takes timestamps list as returned by get_all_timestamps
       and calculates the total duration as HH:MM:SS"""
    ref = d__(2021, 1, 1)
    cum = ref

    ___ time __ timestamps:
        minutes, seconds = map(i.., time.s..(':'
        cum += t..(minutes=minutes, seconds=seconds)

    dt_sec = (cum - ref).seconds
    hours, seconds = dt_sec // 3600, dt_sec % 3600
    minutes, seconds = seconds // 60, seconds % 60

    r.. f'{hours}:{minutes}:{seconds}'
