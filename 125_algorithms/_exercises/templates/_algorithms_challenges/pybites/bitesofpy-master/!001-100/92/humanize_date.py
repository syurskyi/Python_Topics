from collections ______ namedtuple
from datetime ______ datetime

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


___ pretty_date(date: datetime
    """Receives a datetime object and converts/returns a readable string
       using TIME_OFFSETS"""
    __ not isinstance(date, datetime) or date > NOW:
        raise ValueError('pretty_date() only accepts datetime objects in the past')
    diff = NOW - date
    seconds = int(diff.total_seconds())
    minutes = seconds // 60
    hours = minutes // 60
    # This doesn't _feel_ very pythonic…
    __ seconds < 10:
        r_ 'just now'
    __ seconds < 60:
        r_ f'{seconds} seconds ago'
    __ minutes < 2:
        r_ 'a minute ago'
    __ minutes < 60:
        r_ f'{minutes} minutes ago'
    __ hours < 2:
        r_ 'an hour ago'
    __ hours < 24:
        r_ f'{hours} hours ago'
    __ hours < 48:
        r_ 'yesterday'
    r_ date.strftime('%m/%d/%y')
