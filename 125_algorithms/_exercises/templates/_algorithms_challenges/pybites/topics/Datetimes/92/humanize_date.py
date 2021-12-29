____ collections _______ n..
____ d__ _______ d__, t..

TimeOffset = n..('TimeOffset', 'offset date_str divider')

NOW = d__.now()
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
    __ n.. isi..(date, d__) o. date > NOW:
        raise ValueError
    elapsed = (NOW - date).total_seconds()
    ___ timeoffset __ TIME_OFFSETS:
        __ elapsed < timeoffset.offset:
            __ timeoffset.divider:
                elapsed = elapsed/timeoffset.divider
            elapsed = int(elapsed)
            r.. timeoffset.date_str.f..(elapsed)
    r.. date.strftime("%m/%d/%y")


dt = d__.now() - t..(days=2, hours=22, minutes=14, seconds=15)
#dt = datetime.now() - timedelta(seconds=125)
#print(dt)
print(pretty_date(dt))