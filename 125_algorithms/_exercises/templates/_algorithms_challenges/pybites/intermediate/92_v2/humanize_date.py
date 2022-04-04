____ c.. _______ n..
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


___ pretty_date(date
    """Receives a datetime object and converts/returns a readable string
       using TIME_OFFSETS"""
    

    __ t..(date) != d__:
        r.. V...("Not a datetime")

    __ date > NOW:
        r.. V...("Invalid date! Date in future!")


    delta = i..((NOW - date).total_seconds


    ___ time_offset,time_string,divider __ TIME_OFFSETS:
        __ delta < time_offset:
            __ divider:
                delta //= divider


            __ '{}' __ time_string:
                r.. time_string.f..(delta)
            ____
                r.. time_string

        
    r.. date.s..("%m/%d/%y")








