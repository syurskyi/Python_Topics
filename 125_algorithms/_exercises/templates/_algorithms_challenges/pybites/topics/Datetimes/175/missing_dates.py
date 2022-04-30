____ d__ _______ d__, t..
____ r__ _______ s..

___ get_missing_dates dates
    """Receives a range of dates and returns a sequence
       of missing datetime.date objects (no worries about order).

       You can assume that the first and last date of the
       range is always present (assumption made in tests).

       See the Bite description and tests for example outputs.
    """
    first_dt m..(dates)
    last_dt m..(dates)
    full_dt [first_dt+t..(i) ___ i __ r..((last_dt-first_dt).days+1)]
    r.. s..(s..(full_dt)-s..(dates


___ _create_dates missing  y.._2019  m.._2
    """Helper function to build up test cases.

       Returns a list of dates omitting days given
       in the missing argument.

       You can optionally specify year and month.
    """
    first date y.._?  m.._?  d.._1)
    last first.r.. m.._?+1 - t.. d.._1

    # always yield first and last, for the in between dates
    # only the ones not in missing
    y.. f..

    ___ day __ r.. ?.d.. + 1 ?.d..
        __ day n.. __ missing
            y.. f...r.. d.._?

    y.. l..


date_list l..(_create_dates([2, 7, 11], 2

#print(type(date_list), len(date_list))
#print(date_list)

print(get_missing_dates(date_list