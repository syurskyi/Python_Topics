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

with open(logfile) as f:
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

    values = line.s..

    date = values[1]

    r.. d__.strptime(date,"%Y-%m-%dT%H:%M:%S")


___ time_between_shutdowns(loglines):
    """TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and
       calculate the timedelta between the first and last one.
       Return this datetime.timedelta object.
    pass
    """
    
    first = N..

    ___ line __ loglines:
        __ 'Shutdown initiated' __ line:
            __ n.. first:
                first = convert_to_datetime(line)
            ____:
                last = convert_to_datetime(line)

    r.. last - first
