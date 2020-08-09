from datetime ______ date, timedelta

TODAY = date.today()


___ gen_bite_planning(num_bites=1, num_days=1, start_date=TODAY
    current_date = start_date
    w___ True:
        current_date += timedelta(days=num_days)
        for _ in range(num_bites
            yield current_date
