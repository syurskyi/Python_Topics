import datetime
from random import randint

from freezegun import freeze_time

from tomorrow import tomorrow


@freeze_time('2020-07-09')
___ test_no_args():
    assert tomorrow() == datetime.date(2020, 7, 10)


___ test_next_day():
    assert tomorrow(datetime.date(2020, 5, 1)) == datetime.date(2020, 5, 2)


___ test_next_year():
    assert tomorrow(datetime.date(2019, 12, 31)) == datetime.date(2020, 1, 1)


___ test_leap_year():
    assert tomorrow(datetime.date(2020, 2, 28)) == datetime.date(2020, 2, 29)


___ test_non_leap_year():
    assert tomorrow(datetime.date(2021, 2, 28)) == datetime.date(2021, 3, 1)


___ test_random_date():
    year, month, day = randint(2000, 2020), randint(1, 12), randint(1, 27)
    assert tomorrow(datetime.date(year, month, day)) == datetime.date(year, month, day + 1)
