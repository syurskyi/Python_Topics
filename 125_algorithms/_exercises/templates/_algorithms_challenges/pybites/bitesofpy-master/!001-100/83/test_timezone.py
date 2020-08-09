from datetime ______ datetime

from Previous.timezone ______ what_time_lives_pybites


___ test_what_time_lives_pybites_spanish_summertime(
    # AUS is 8 hours ahead of ES
    naive_utc_dt = datetime(2018, 4, 27, 22, 55, 0)
    aus_dt, es_dt = what_time_lives_pybites(naive_utc_dt)

    assert aus_dt.year __ 2018
    assert aus_dt.month __ 4
    assert aus_dt.day __ 28
    assert aus_dt.hour __ 8
    assert aus_dt.minute __ 55

    assert es_dt.year __ 2018
    assert es_dt.month __ 4
    assert es_dt.day __ 28
    assert es_dt.hour __ 0
    assert es_dt.minute __ 55


___ test_what_time_lives_pybites_spanish_wintertime(
    # AUS is 10 hours ahead of ES
    naive_utc_dt = datetime(2018, 11, 1, 14, 10, 0)
    aus_dt, es_dt = what_time_lives_pybites(naive_utc_dt)

    assert aus_dt.year __ 2018
    assert aus_dt.month __ 11
    assert aus_dt.day __ 2
    assert aus_dt.hour __ 1
    assert aus_dt.minute __ 10

    assert es_dt.year __ 2018
    assert es_dt.month __ 11
    assert es_dt.day __ 1
    assert es_dt.hour __ 15
    assert es_dt.minute __ 10