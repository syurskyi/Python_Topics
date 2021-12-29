from datetime import timedelta


___ get_missing_dates(dates):
    """Receives a range of dates and returns a sequence
       of missing datetime.date objects (no worries about order).

       You can assume that the first and last date of the
       range is always present (assumption made in tests).

       See the Bite description and tests for example outputs.
    """
    first, last = min(dates), max(dates)
    diff = (last - first).days

    missing = list()

    for k in range(1, diff + 1):
        chk_date = first + timedelta(days=k)

        __ chk_date not in dates:
            missing.append(chk_date)

    return missing
