from datetime import timedelta
def get_missing_dates(dates):
    """Receives a range of dates and returns a sequence
       of missing datetime.date objects (no worries about order).

       You can assume that the first and last date of the
       range is always present (assumption made in tests).

       See the Bite description and tests for example outputs.
    """


    dates = sorted(dates)

    missing = [] 
    for i in range(len(dates) - 1):
        date = dates[i]

        next_date = date + timedelta(days=1)

        while next_date != dates[i +1]:
            missing.append(next_date)
            next_date += timedelta(days=1)
    

        
    return missing







