____ d__ _______ d__
_______ os
_______ urllib.request

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
tmp = os.getenv("TMP", "/tmp")
logfile = os.path.j..(tmp, 'log')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/messages.log',
    logfile
)

w__ open(logfile) __ f:
    loglines = f.readlines()

___ convert_to_datetime(line):
    """
    Extract timestamp from logline and convert it to a datetime object.
    For example calling the function with:
    INFO 2014-07-03T23:27:51 supybot Shutdown complete.
    returns: datetime(2014, 7, 3, 23, 27, 51)
    """
    d = line.s.. [1]
    r.. d__.strptime(d, '%Y-%m-%dT%H:%M:%S')


___ time_between_shutdowns(loglines):
    """
    Extract shutdown events ("Shutdown initiated") from loglines and
    calculate the timedelta between the first and last one.
    Return this datetime.timedelta object.
    """
    lines = [l ___ l __ loglines __ l.__contains__(SHUTDOWN_EVENT)]
    start_date = convert_to_datetime(lines[0])
    end_date = convert_to_datetime(lines[-1])
    r.. end_date - start_date