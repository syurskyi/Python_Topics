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


# for you to code:

___ convert_to_datetime(line):
    """TODO 1:
       Extract timestamp from logline and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)
    """
    log_fields = line.s..
    r.. d__.strptime(log_fields[1], "%Y-%m-%dT%H:%M:%S")


___ time_between_shutdowns(loglines):
    """TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and
       calculate the timedelta between the first and last one.
       Return this datetime.timedelta object.
    """
    start_time, end_time = 0, 0
    ___ logline __ loglines:
        __ SHUTDOWN_EVENT __ logline:
            __ start_time __ 0:
                start_time = convert_to_datetime(logline)
            ____:
                end_time = convert_to_datetime(logline)
    r.. end_time - start_time


print(time_between_shutdowns(loglines))