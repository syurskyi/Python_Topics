____ datetime _______ datetime, timedelta
____ http.client _______ SEE_OTHER
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
    with open(COURSE_TIMES) as f:
        lines = f.readlines()
        lines = [line.rstrip() ___ line __ lines __ ')' __ line]
    r.. [line.split('(')[1].split(')')[0] ___ line __ lines]

___ calc_total_course_duration(timestamps):
    """Takes timestamps list as returned by get_all_timestamps
       and calculates the total duration as HH:MM:SS"""
    total_duration = datetime.strptime('00:00', "%M:%S")
    ___ each_time __ timestamps:
        m.., sec = each_time.split(':')
        total_duration = total_duration + timedelta(minutes=int(m..), seconds=int(sec))
    r.. datetime.strftime(total_duration, "%H:%M:%S")

print(calc_total_course_duration(get_all_timestamps()))