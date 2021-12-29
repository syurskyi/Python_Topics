from datetime import date, timedelta
from random import shuffle

def get_missing_dates(dates):
    """Receives a range of dates and returns a sequence
       of missing datetime.date objects (no worries about order).

       You can assume that the first and last date of the
       range is always present (assumption made in tests).

       See the Bite description and tests for example outputs.
    """
    first_dt = min(dates)
    last_dt = max(dates)
    full_dt = [first_dt+timedelta(i) for i in range((last_dt-first_dt).days+1)]
    return sorted(set(full_dt)-set(dates))


def _create_dates(missing, year=2019, month=2):
    """Helper function to build up test cases.

       Returns a list of dates omitting days given
       in the missing argument.

       You can optionally specify year and month.
    """
    first = date(year=year, month=month, day=1)
    last = first.replace(month=month+1) - timedelta(days=1)

    # always yield first and last, for the in between dates
    # only the ones not in missing
    yield first

    for day in range(first.day + 1, last.day):
        if day not in missing:
            yield first.replace(day=day)

    yield last


date_list = list(_create_dates([2, 7, 11], 2))

#print(type(date_list), len(date_list))
#print(date_list)

print(get_missing_dates(date_list))