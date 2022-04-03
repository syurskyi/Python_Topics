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
    with open(COURSE_TIMES) as file:
        course_timestamps = []
        file_lines = file.readlines()
        for line in file_lines:
            ts = re.findall(r"(\d{1,2}?:\d{1,2})", line)
            if ts:
                course_timestamps.append(ts[0])

        return course_timestamps


def calc_total_course_duration(timestamps):
    """Takes timestamps list as returned by get_all_timestamps
       and calculates the total duration as HH:MM:SS"""
    dt_conversion = [datetime.strptime(ts, '%M:%S') for ts in timestamps]
    baseline = datetime(1900, 1, 1, 0, 0, 0)
    for course_dt in dt_conversion:
        baseline = baseline + timedelta(minutes=course_dt.minute, seconds=course_dt.second) 

    return baseline.strftime('%-H:%M:%S')


#if __name__ == "__main__":
    #print(get_all_timestamps())
    #print(calc_total_course_duration(get_all_timestamps()))