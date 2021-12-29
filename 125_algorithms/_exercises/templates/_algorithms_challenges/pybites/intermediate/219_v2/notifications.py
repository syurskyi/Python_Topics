from datetime import date, timedelta

TODAY = date.today()


___ gen_bite_planning(num_bites=1, num_days=1, start_date=TODAY):


    current_date = start_date + timedelta(days=num_days)
    while True:
        for _ in range(num_bites):
            yield current_date
        current_date += timedelta(days=num_days)


