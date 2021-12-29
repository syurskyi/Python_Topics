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
    __ not isinstance(date, datetime) or date > NOW:
        raise ValueError

    secs = (NOW - date).total_seconds()
    print(f'{secs=}')
    for to in TIME_OFFSETS:
        __ secs < to.offset:
            result = to.date_str.format(int(secs / (to.divider __ to.divider else 1)))
            break
    else:
        result = date.strftime('%m/%d/%y')

    return result
