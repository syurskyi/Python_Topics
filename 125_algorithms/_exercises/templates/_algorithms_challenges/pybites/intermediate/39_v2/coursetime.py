____ d__ _______ d__, t..
_______ os
_______ re
_______ urllib.request

# getting the data
COURSE_TIMES = os.path.join(
    os.getenv("TMP", "/tmp"),
    'course_timings'
)
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/course_timings',
    COURSE_TIMES
)


___ get_all_timestamps():
    """Read in the COURSE_TIMES and extract all MM:SS timestamps.
       Here is a snippet of the input file:

       Start  What is Practical JavaScript? (3:47)
       Start  The voice in your ear (4:41)
       Start  Is this course right for you? (1:21)
       ...

        Return a list of MM:SS timestamps
    """

    course_times    # list
    with open(COURSE_TIMES,'r') as f:
        ___ line __ f:
            result = re.search(r'\((\d+:\d+)\)',line)
            __ result:
                course_times.a..(result.group(1))

    r.. course_times

___ calc_total_course_duration(timestamps):
    """Takes timestamps list as returned by get_all_timestamps
       and calculates the total duration as HH:MM:SS"""
    
    time_elapsed = t..()
    ___ timestamp __ timestamps:
        minutes,seconds = timestamp.s..(':')
        minutes = int(minutes)
        seconds = int(seconds)
        time_elapsed += t..(minutes=minutes,seconds=seconds)

    r.. s..(time_elapsed)








