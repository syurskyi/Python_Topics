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

___ convert_to_datetime(line):
    """
    Extract timestamp from logline and convert it to a datetime object.
    For example calling the function with:
    INFO 2014-07-03T23:27:51 supybot Shutdown complete.
    returns: datetime(2014, 7, 3, 23, 27, 51)
    """
    d = line.split()[1]
    return datetime.strptime(d, '%Y-%m-%dT%H:%M:%S')


___ time_between_shutdowns(loglines):
    """
    Extract shutdown events ("Shutdown initiated") from loglines and
    calculate the timedelta between the first and last one.
    Return this datetime.timedelta object.
    """
    lines = [l for l in loglines __ l.__contains__(SHUTDOWN_EVENT)]
    start_date = convert_to_datetime(lines[0])
    end_date = convert_to_datetime(lines[-1])
    return end_date - start_date