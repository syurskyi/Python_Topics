from datetime import datetime, timedelta, time
import os
import re
import urllib.request

# https://stackoverflow.com/questions/100210/what-is-the-standard-way-to-add-n-seconds-to-datetime-time-in-python

# getting the data
COURSE_TIMES = os.path.join(
    os.getenv("TMP", "/tmp"),
    'course_timings'
)
urllib.request.urlretrieve(
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
    with open(COURSE_TIMES, 'r') as f:
        result = []
        for line in f:
            timestamp = re.findall(r'(\d{1,2}:\d{1,2})', line)
            if timestamp:
                result.append(timestamp[0])
        print(result)
    return result


def calc_total_course_duration(timestamps):
    """Takes timestamps list as returned by get_all_timestamps
       and calculates the total duration as HH:MM:SS"""
    sum = datetime(year=2000, month=1, day=1, hour=0, minute=0, second=0)
    s = sum + timedelta(hours=0, minutes=0, seconds=10)
    for item in timestamps:
        sum = sum + timedelta(hours=0, minutes=int(item.split(':')[0]), seconds=int(item.split(':')[1]))
    return(str(sum.time()))

"""
def get_all_timestamps():
    Read in the COURSE_TIMES and extract all MM:SS timestamps.
       Here is a snippet of the input file:

       Start  What is Practical JavaScript? (3:47)
       Start  The voice in your ear (4:41)
       Start  Is this course right for you? (1:21)
       ...

        Return a list of MM:SS timestamps
    
    with open(COURSE_TIMES) as f:
        content = f.read()
        return re.findall(r'\d+:\d+', content)


def calc_total_course_duration(timestamps):
    Takes timestamps list as returned by get_all_timestamps
       and calculates the total duration as HH:MM:SS
    result = timedelta(minutes=0, seconds=0)

    for mm_ss in timestamps:
        minutes, seconds = mm_ss.split(':')
        result += timedelta(minutes=int(minutes), seconds=int(seconds))

    return str(result)
"""


get_all_timestamps()
print(calc_total_course_duration(get_all_timestamps()))