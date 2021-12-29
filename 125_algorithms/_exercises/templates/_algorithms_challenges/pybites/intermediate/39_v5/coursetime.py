____ datetime _______ datetime, timedelta
_______ os
_______ re
_______ urllib.request

# getting the data
COURSE_TIMES = os.path.join('/tmp', 'course_timings')
urllib.request.urlretrieve('http://bit.ly/2Eb0iQF', COURSE_TIMES)


___ get_all_timestamps():
    """Read in the COURSE_TIMES and extract all MM:SS timestamps.
       Here is a snippet of the input file:

       Start  What is Practical JavaScript? (3:47)
       Start  The voice in your ear (4:41)
       Start  Is this course right for you? (1:21)
       ...

        Return a list of MM:SS timestamps
    """
    result    # list
    with open(COURSE_TIMES) as ct:
        ___ line __ ct.readlines():
            times = re.findall(r'\((\d\d?:\d\d)\)', line)
            __ l..(times) > 0:
                result.a..(times[0])
    r.. result


___ calc_total_course_duration(timestamps):
    """Takes timestamps list as returned by get_all_timestamps
       and calculates the total duration as HH:MM:SS"""
    total_time = s..(timedelta(minutes=xt.minute, seconds=xt.second).total_seconds()
                     ___ t __ timestamps
                     ___ xt __ [datetime.strptime(t, '%M:%S')])
    r.. str(timedelta(seconds=total_time))
