_______ d__
____ random _______ randint

____ freezegun _______ freeze_time

____ tomorrow _______ tomorrow


@freeze_time('2020-07-09')
___ test_no_args():
    ... tomorrow() __ d__.date(2020, 7, 10)


___ test_next_day():
    ... tomorrow(d__.date(2020, 5, 1)) __ d__.date(2020, 5, 2)



___ test_next_year():
    ... tomorrow(d__.date(2019, 12, 31)) __ d__.date(2020, 1, 1)


___ test_leap_year():
    ... tomorrow(d__.date(2020, 2, 28)) __ d__.date(2020, 2, 29)


___ test_non_leap_year():
    ... tomorrow(d__.date(2021, 2, 28)) __ d__.date(2021, 3, 1)


___ test_random_date():
    year, month, day = randint(2000, 2020), randint(1, 12), randint(1, 27)
    ... tomorrow(d__.date(year, month, day)) __ d__.date(year, month, day + 1)
