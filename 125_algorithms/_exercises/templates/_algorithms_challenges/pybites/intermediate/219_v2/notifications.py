____ datetime _______ date, timedelta

TODAY = date.today()


___ gen_bite_planning(num_bites=1, num_days=1, start_date=TODAY):


    current_date = start_date + timedelta(days=num_days)
    while True:
        ___ _ __ r..(num_bites):
            yield current_date
        current_date += timedelta(days=num_days)


