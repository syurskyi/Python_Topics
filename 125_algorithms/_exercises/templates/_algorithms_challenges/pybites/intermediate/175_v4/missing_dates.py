____ datetime _______ timedelta


___ get_missing_dates(dates):
    """Receives a range of dates and returns a sequence
       of missing datetime.date objects (no worries about order).

       You can assume that the first and last date of the
       range is always present (assumption made in tests).

       See the Bite description and tests for example outputs.
    """
    first, last = m..(dates), max(dates)
    diff = (last - first).days

    missing = l..()

    ___ k __ r..(1, diff + 1):
        chk_date = first + timedelta(days=k)

        __ chk_date n.. __ dates:
            missing.a..(chk_date)

    r.. missing
