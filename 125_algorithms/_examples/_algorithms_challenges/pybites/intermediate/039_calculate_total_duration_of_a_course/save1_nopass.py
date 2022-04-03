from datetime import datetime, timedelta
import os
import re
import u__.r..

# getting the data
COURSE_TIMES = os.path.join(
    os.getenv("TMP", "/tmp"),
    'course_timings'
)
u__.r...u..(
    'https://bites-data.s3.us-east-2.amazonaws.com/course_timings',
    COURSE_TIMES
)


def get_all_timestamps():
    """Read in the COURSE_TIMES and extract all MM:SS timestamps.
       Here is a snippet of the input file:

       Start  What is Practical JavaScript? (3:47)
       Start  The voice in your ear (4:41)
       Start  Is this course right for you? (1:21)
       ...

        Return a list of MM:SS timestamps
    """
    with open(COURSE_TIMES) as f:
        file = f.readlines()

    r = re.compile(r'\(\d+:\d+\)')

    l = []
    for t in file:
        t = re.search(r, t)
        if t != None:
            t = t.group()
            l.append(re.sub(r'[\(\)]','', t))

    return l


def calc_total_course_duration(timestamps):
    """Takes timestamps list as returned by get_all_timestamps
       and calculates the total duration as HH:MM:SS"""
    l = [datetime.strptime(date, '%M:%S') for date in timestamps]

    for t in l:
        mins += t.minute
        secs += t.second
    
    deltas = [timedelta(seconds=t.second, minutes=t.minute)
              for t in l]

    return sum(deltas, timedelta())