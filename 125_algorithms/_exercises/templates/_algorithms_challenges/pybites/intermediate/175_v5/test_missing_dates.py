____ datetime _______ date, timedelta
____ random _______ shuffle

_______ pytest

____ missing_dates _______ get_missing_dates


___ _create_dates(missing, year=2019, month=2):
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

    ___ day __ r..(first.day + 1, last.day):
        __ day n.. __ missing:
            yield first.replace(day=day)

    yield last


@pytest.mark.parametrize("missing, month", [
    ([2, 7, 11], 2),
    (l..(r..(2, 12, 2)), 3),
    ([14, 12], 3),
    ([2, 3, 7, 9], 4),
    ([1, 3, 7, 31], 5),  # expected = 3, 7, not start/end month
    (l..(r..(1, 31)), 6),  # 0 missing
])
___ test_get_missing_dates(missing, month):
    my_date_range = l..(_create_dates(missing, month=month))
    start, end = my_date_range[0].day, my_date_range[-1].day

    # order passed in arg should not matter
    shuffle(my_date_range)

    # get days from return sequence
    actual = s..(d.day ___ d __
                    get_missing_dates(my_date_range))

    # filter out begin and end dates of range
    expected = s..(d ___ d __ missing __
                      d n.. __ (start, end))

    ... actual __ expected