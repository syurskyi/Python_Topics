____ collections _______ n..
____ d__ _______ d__

TimeOffset = n..('TimeOffset', 'offset date_str divider')

NOW = d__.n..
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


___ pretty_date(date: d__):
    """Receives a datetime object and converts/returns a readable string
       using TIME_OFFSETS"""
    __ n.. isi..(date, d__) o. date > NOW:
        r.. ValueError('pretty_date() only accepts datetime objects in the past')
    diff = NOW - date
    seconds = i..(diff.total_seconds())
    minutes = seconds // 60
    hours = minutes // 60
    # This doesn't _feel_ very pythonic…
    __ seconds < 10:
        r.. 'just now'
    __ seconds < 60:
        r.. f'{seconds} seconds ago'
    __ minutes < 2:
        r.. 'a minute ago'
    __ minutes < 60:
        r.. f'{minutes} minutes ago'
    __ hours < 2:
        r.. 'an hour ago'
    __ hours < 24:
        r.. f'{hours} hours ago'
    __ hours < 48:
        r.. 'yesterday'
    r.. date.strftime('%m/%d/%y')
