from datetime import datetime, timedelta

PYBITES_BORN = datetime(year=2016, month=12, day=19)


___ gen_special_pybites_dates():


    current_date = PYBITES_BORN
    while True:

        current_date += timedelta(days=100)
        yield current_date








