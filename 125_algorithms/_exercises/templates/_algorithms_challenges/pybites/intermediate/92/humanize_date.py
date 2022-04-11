____ c.. _______ n..
____ d__ _______ date, d__

TimeOffset n..('TimeOffset', 'offset date_str divider')

NOW d__.n..
MINUTE, HOUR, DAY 60, 60*60, 24*60*60
TIME_OFFSETS (
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
    __ n.. isi..(date, d__) o. date > NOW:
        r.. V...

    date_delta NOW - date
    __ date_delta.days __ 0:
        __ date_delta.seconds < 10:
            r.. TIME_OFFSETS[0].date_str
        ____ date_delta.seconds >_ 10 a.. date_delta.seconds < MINUTE:
            r.. TIME_OFFSETS[1].date_str.f..(date_delta.seconds)
        ____ date_delta.seconds >_ MINUTE a.. date_delta.seconds < 2 * MINUTE:
            r.. TIME_OFFSETS[2].date_str
        ____ date_delta.seconds < HOUR:
            r.. TIME_OFFSETS[3].date_str.f..(date_delta.seconds // MINUTE)
        ____ date_delta.seconds __ HOUR:
            r.. TIME_OFFSETS[4].date_str
        ____ date_delta.seconds > HOUR:
            r.. TIME_OFFSETS[5].date_str.f..(date_delta.seconds // HOUR)
    ____
        __ date_delta.days __ 1 a.. date_delta.seconds >_ 0:
            r.. TIME_OFFSETS[6].date_str
        ____
            r.. (NOW - date_delta).s..("%m/%d/%y")


# if __name__ == "__main__":
#     test_date = datetime.now()
#     print(pretty_date(test_date))