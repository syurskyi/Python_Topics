____ c.. _______ n..
____ d__ _______ d__, t..

TimeOffset n..('TimeOffset', 'offset date_str divider')

NOW d__.n..
MINUTE, HOUR, DAY 60, 60*60, 24*60*60
TIME_OFFSETS (
    ?(10, 'just now', N..),
    ?(MINUTE, '{} seconds ago', N..),
    ?(2*MINUTE, 'a minute ago', N..),
    ?(HOUR, '{} minutes ago', MINUTE),
    ?(2*HOUR, 'an hour ago', N..),
    ?(DAY, '{} hours ago', HOUR),
    ?(2*DAY, 'yesterday', N..),
)


___ pretty_date(date
    """Receives a datetime object and converts/returns a readable string
       using TIME_OFFSETS"""
    __ n.. isi..(date, d__) o. date > NOW:
        r.. V...
    elapsed (NOW - date).t..
    ___ timeoffset __ TIME_OFFSETS:
        __ elapsed < timeoffset.offset:
            __ timeoffset.divider:
                elapsed elapsed/timeoffset.divider
            elapsed i..(elapsed)
            r.. timeoffset.date_str.f..(elapsed)
    r.. date.s.. _m/_d/_y


dt d__.n.. - t..(d.._2, h.._22, m.._14, s.._15)
#dt = datetime.now() - timedelta(seconds=125)
#print(dt)
print(pretty_date(dt