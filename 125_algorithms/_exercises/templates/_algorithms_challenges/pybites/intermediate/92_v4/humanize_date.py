____ collections _______ namedtuple
____ datetime _______ datetime

TimeOffset = namedtuple('TimeOffset', 'offset date_str divider')

NOW = datetime.now()
MINUTE, HOUR, DAY = 60, 60*60, 24*60*60
TIME_OFFSETS = (
    TimeOffset(10, 'just now', N..),
    TimeOffset(MINUTE, '{} seconds ago', N..),
    TimeOffset(2*MINUTE, 'a minute ago', N..),
    TimeOffset(HOUR, '{} minutes ago', MINUTE),
    TimeOffset(2*HOUR, 'an hour ago', N..),
    TimeOffset(DAY, '{} hours ago', HOUR),
    TimeOffset(2*DAY, 'yesterday', N..),
)


___ pretty_date(date):
    """Receives a datetime object and converts/returns a readable string
       using TIME_OFFSETS"""
    __ n.. isi..(date, datetime) o. date > NOW:
        raise ValueError

    secs = (NOW - date).total_seconds()
    print(f'{secs=}')
    ___ to __ TIME_OFFSETS:
        __ secs < to.offset:
            result = to.date_str.format(int(secs / (to.divider __ to.divider ____ 1)))
            break
    ____:
        result = date.strftime('%m/%d/%y')

    r.. result
