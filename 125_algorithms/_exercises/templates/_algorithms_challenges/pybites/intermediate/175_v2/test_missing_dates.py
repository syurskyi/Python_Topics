____ d__ _______ date, t..
____ r__ _______ shuffle

_______ p__

____ missing_dates _______ get_missing_dates


___ _create_dates(missing, year=2019,  m.._2
    """Helper function to build up test cases.

       Returns a list of dates omitting days given
       in the missing argument.

       You can optionally specify year and month.
    """
    first = date y.._year,  m.._month,  d.._1)
    last = first.r..( m.._month+1) - t..(d.._1)

    # always yield first and last, for the in between dates
    # only the ones not in missing
    y.. first

    ___ day __ r..(first.day + 1, last.day
        __ day n.. __ missing:
            y.. first.r..( d.._day)

    y.. last


?p__.m__.p.("missing, month", [
    ([2, 7, 11], 2),
    (l..(r..(2, 12, 2, 3),
    ([14, 12], 3),
    ([2, 3, 7, 9], 4),
    ([1, 3, 7, 31], 5),  # expected = 3, 7, not start/end month
    (l..(r..(1, 31, 6),  # 0 missing
])
___ test_get_missing_dates(missing, month
    my_date_range = l..(_create_dates(missing,  m.._month
    start, end = my_date_range[0].day, my_date_range[-1].day

    # order passed in arg should not matter
    shuffle(my_date_range)

    # get days from return sequence
    actual = s..(d.day ___ d __
                    get_missing_dates(my_date_range

    # filter out begin and end dates of range
    expected = s..(d ___ d __ missing __
                      d n.. __ (start, end

    ... actual __ expected
