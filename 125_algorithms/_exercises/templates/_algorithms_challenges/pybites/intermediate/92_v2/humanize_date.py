from collections import namedtuple
from datetime import datetime

TimeOffset = namedtuple('TimeOffset', 'offset date_str divider')

NOW = datetime.now()
MINUTE, HOUR, DAY = 60, 60*60, 24*60*60
TIME_OFFSETS = (
    TimeOffset(10, 'just now', None),
    TimeOffset(MINUTE, '{} seconds ago', None),
    TimeOffset(2*MINUTE, 'a minute ago', None),
    TimeOffset(HOUR, '{} minutes ago', MINUTE),
    TimeOffset(2*HOUR, 'an hour ago', None),
    TimeOffset(DAY, '{} hours ago', HOUR),
    TimeOffset(2*DAY, 'yesterday', None),
)


___ pretty_date(date):
    """Receives a datetime object and converts/returns a readable string
       using TIME_OFFSETS"""
    

    __ type(date) != datetime:
        raise ValueError("Not a datetime")

    __ date > NOW:
        raise ValueError("Invalid date! Date in future!")


    delta = int((NOW - date).total_seconds())


    for time_offset,time_string,divider in TIME_OFFSETS:
        __ delta < time_offset:
            __ divider:
                delta //= divider


            __ '{}' in time_string:
                return time_string.format(delta)
            else:
                return time_string

        
    return date.strftime("%m/%d/%y")








