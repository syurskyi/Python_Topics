from datetime ______ timedelta


___ get_missing_dates(dates
    """Receives a range of dates and returns a sequence
       of missing datetime.date objects (no worries about order).

       You can assume that the first and last date of the
       range is always present (assumption made in tests).

       See the Bite description and tests for example outputs.
    """
    dt = sorted(dates)
    start_date, end_date = dt[0], dt[-1]
    rng: timedelta = end_date - start_date
    r_ [start_date + timedelta(d)
            ___ d __ range(rng.days)
            __ (start_date + timedelta(d)) not __ dt]
