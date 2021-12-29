from collections import namedtuple
from datetime import datetime, timedelta

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


def pretty_date(date):
    """Receives a datetime object and converts/returns a readable string
       using TIME_OFFSETS"""
    if not isinstance(date, datetime) or date > NOW:
        raise ValueError
    elapsed = (NOW - date).total_seconds()
    for timeoffset in TIME_OFFSETS:
        if elapsed < timeoffset.offset:
            if timeoffset.divider:
                elapsed = elapsed/timeoffset.divider
            elapsed = int(elapsed)
            return timeoffset.date_str.format(elapsed)
    return date.strftime("%m/%d/%y")


dt = datetime.now() - timedelta(days=2, hours=22, minutes=14, seconds=15)
#dt = datetime.now() - timedelta(seconds=125)
#print(dt)
print(pretty_date(dt))