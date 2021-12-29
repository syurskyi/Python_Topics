from collections import namedtuple
from datetime import date, datetime

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

    date_delta = NOW - date
    __ date_delta.days == 0:
        __ date_delta.seconds < 10:
            return TIME_OFFSETS[0].date_str
        elif date_delta.seconds >= 10 and date_delta.seconds < MINUTE:
            return TIME_OFFSETS[1].date_str.format(date_delta.seconds)
        elif date_delta.seconds >= MINUTE and date_delta.seconds < 2 * MINUTE:
            return TIME_OFFSETS[2].date_str
        elif date_delta.seconds < HOUR:
            return TIME_OFFSETS[3].date_str.format(date_delta.seconds // MINUTE)
        elif date_delta.seconds == HOUR:
            return TIME_OFFSETS[4].date_str
        elif date_delta.seconds > HOUR:
            return TIME_OFFSETS[5].date_str.format(date_delta.seconds // HOUR)
    else:
        __ date_delta.days == 1 and date_delta.seconds >= 0:
            return TIME_OFFSETS[6].date_str
        else:
            return (NOW - date_delta).strftime("%m/%d/%y")


# if __name__ == "__main__":
#     test_date = datetime.now()
#     print(pretty_date(test_date))