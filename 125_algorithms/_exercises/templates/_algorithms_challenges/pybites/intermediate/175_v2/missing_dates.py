____ d__ _______ t..
___ get_missing_dates(dates):
    """Receives a range of dates and returns a sequence
       of missing datetime.date objects (no worries about order).

       You can assume that the first and last date of the
       range is always present (assumption made in tests).

       See the Bite description and tests for example outputs.
    """


    dates = s..(dates)

    missing    # list
    ___ i __ r..(l..(dates) - 1):
        date = dates[i]

        next_date = date + t..(days=1)

        w.... next_date != dates[i +1]:
            missing.a..(next_date)
            next_date += t..(days=1)
    

        
    r.. missing







