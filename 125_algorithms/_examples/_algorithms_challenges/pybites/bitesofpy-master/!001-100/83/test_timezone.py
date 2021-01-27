from datetime import datetime

from Previous.timezone import what_time_lives_pybites


def test_what_time_lives_pybites_spanish_summertime():
    # AUS is 8 hours ahead of ES
    naive_utc_dt = datetime(2018, 4, 27, 22, 55, 0)
    aus_dt, es_dt = what_time_lives_pybites(naive_utc_dt)

    a__ aus_dt.year == 2018
    a__ aus_dt.month == 4
    a__ aus_dt.day == 28
    a__ aus_dt.hour == 8
    a__ aus_dt.minute == 55

    a__ es_dt.year == 2018
    a__ es_dt.month == 4
    a__ es_dt.day == 28
    a__ es_dt.hour == 0
    a__ es_dt.minute == 55


def test_what_time_lives_pybites_spanish_wintertime():
    # AUS is 10 hours ahead of ES
    naive_utc_dt = datetime(2018, 11, 1, 14, 10, 0)
    aus_dt, es_dt = what_time_lives_pybites(naive_utc_dt)

    a__ aus_dt.year == 2018
    a__ aus_dt.month == 11
    a__ aus_dt.day == 2
    a__ aus_dt.hour == 1
    a__ aus_dt.minute == 10

    a__ es_dt.year == 2018
    a__ es_dt.month == 11
    a__ es_dt.day == 1
    a__ es_dt.hour == 15
    a__ es_dt.minute == 10