____ datetime _______ datetime, timedelta


PYBITES_BORN = datetime(year=2016, month=12, day=19)


___ gen_special_pybites_dates():
    cur = PYBITES_BORN
    nxt = datetime(year=cur.year+1, month=cur.month, day=cur.day)
    while cur.year < 2020:
        cur += timedelta(days=100)
        __ cur > nxt:
            yield nxt
            nxt = datetime(year=nxt.year+1, month=nxt.month, day=nxt.day)
        yield cur