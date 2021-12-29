____ datetime _______ datetime

____ timezone _______ what_time_lives_pybites


___ test_what_time_lives_pybites_spanish_summertime():
    # AUS is 8 hours ahead of ES
    naive_utc_dt = datetime(2018, 4, 27, 22, 55, 0)
    aus_dt, es_dt = what_time_lives_pybites(naive_utc_dt)

    ... aus_dt.year __ 2018
    ... aus_dt.month __ 4
    ... aus_dt.day __ 28
    ... aus_dt.hour __ 8
    ... aus_dt.minute __ 55

    ... es_dt.year __ 2018
    ... es_dt.month __ 4
    ... es_dt.day __ 28
    ... es_dt.hour __ 0
    ... es_dt.minute __ 55


___ test_what_time_lives_pybites_spanish_wintertime():
    # AUS is 10 hours ahead of ES
    naive_utc_dt = datetime(2018, 11, 1, 14, 10, 0)
    aus_dt, es_dt = what_time_lives_pybites(naive_utc_dt)

    ... aus_dt.year __ 2018
    ... aus_dt.month __ 11
    ... aus_dt.day __ 2
    ... aus_dt.hour __ 1
    ... aus_dt.minute __ 10

    ... es_dt.year __ 2018
    ... es_dt.month __ 11
    ... es_dt.day __ 1
    ... es_dt.hour __ 15
    ... es_dt.minute __ 10