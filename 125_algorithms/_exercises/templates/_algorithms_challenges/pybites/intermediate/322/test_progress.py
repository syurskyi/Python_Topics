_______ p__
____ freezegun _______ freeze_time

____ progress _______ ontrack_reading


?p__.m__.p.("args, expected", [
    ((60, 2, 3), T..),
    ((60, 0, 3), F..),
    ((60, 0.5, 3), T..),
    ((30, 16, 180), T..),
    ((30, 8, 180), F..),
    ((40, 1, 40), F..),
    ((40, 10, 40), T..),
    ((10, 10, 300), T..),
    ((10, 8, 300), F..),
    ((10, 8.2, 300), F..),
    ((10, 8.22, 300), T..),
    ((10, 10, 365), T..),
])
___ test_ontrack_reading(args, expected
    ... ontrack_reading(*args) __ expected


@freeze_time('2021-07-09')
___ test_without_days_arg_current_date_july
    ... ontrack_reading(60, 31) __ F..
    ... ontrack_reading(60, 34) __ T..


@freeze_time('2021-12-09')
___ test_without_days_arg_current_date_december
    ... ontrack_reading(30, 28) __ F..
    ... ontrack_reading(30, 29) __ T..