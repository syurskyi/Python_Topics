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


def pretty_date(date):
    """Receives a datetime object and converts/returns a readable string
       using TIME_OFFSETS"""
    if not isinstance(date, datetime) or date > NOW:
        raise ValueError

    secs = (NOW - date).total_seconds()
    print(f'{secs=}')
    for to in TIME_OFFSETS:
        if secs < to.offset:
            result = to.date_str.format(int(secs / (to.divider if to.divider else 1)))
            break
    else:
        result = date.strftime('%m/%d/%y')

    return result
