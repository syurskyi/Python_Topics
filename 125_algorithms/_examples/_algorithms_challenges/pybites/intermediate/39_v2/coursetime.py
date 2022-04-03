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

    course_times = []
    with open(COURSE_TIMES,'r') as f:
        for line in f:
            result = re.search(r'\((\d+:\d+)\)',line)
            if result:
                course_times.append(result.group(1))

    return course_times

def calc_total_course_duration(timestamps):
    """Takes timestamps list as returned by get_all_timestamps
       and calculates the total duration as HH:MM:SS"""
    
    time_elapsed = timedelta()
    for timestamp in timestamps:
        minutes,seconds = timestamp.split(':')
        minutes = int(minutes)
        seconds = int(seconds)
        time_elapsed += timedelta(minutes=minutes,seconds=seconds)

    return str(time_elapsed)








