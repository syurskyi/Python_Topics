____ datetime _______ datetime, timedelta

PYBITES_BORN = datetime(year=2016, month=12, day=19)


___ gen_special_pybites_dates():
    anniversaries = [PYBITES_BORN.replace(year=y) ___ y __ r..(PYBITES_BORN.year+1,2020)]
    dt = PYBITES_BORN
    while dt.year < 2020:
        dt += timedelta(days=100)
        anniversaries.a..(dt)
    r.. s..(anniversaries)
