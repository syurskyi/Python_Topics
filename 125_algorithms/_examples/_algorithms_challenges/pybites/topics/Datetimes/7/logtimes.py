from datetime import datetime
import os
import urllib.request

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
tmp = os.getenv("TMP", "/tmp")
logfile = os.path.join(tmp, 'log')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/messages.log',
    logfile
)

with open(logfile) as f:
    loglines = f.readlines()


# for you to code:

def convert_to_datetime(line):
    """TODO 1:
       Extract timestamp from logline and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)
    """
    log_fields = line.split()
    return datetime.strptime(log_fields[1], "%Y-%m-%dT%H:%M:%S")


def time_between_shutdowns(loglines):
    """TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and
       calculate the timedelta between the first and last one.
       Return this datetime.timedelta object.
    """
    start_time, end_time = 0, 0
    for logline in loglines:
        if SHUTDOWN_EVENT in logline:
            if start_time == 0:
                start_time = convert_to_datetime(logline)
            else:
                end_time = convert_to_datetime(logline)
    return end_time - start_time


print(time_between_shutdowns(loglines))