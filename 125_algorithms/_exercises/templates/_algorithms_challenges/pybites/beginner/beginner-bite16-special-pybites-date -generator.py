'''
Write a generator that returns special dates for PyBites:

Every year mark counting from PYBITES_BORN date
Every 100 days mark counting from PYBITES_BORN
See the tests for more details how your code will be tested: as this is a beginner's
challenge we only calculate a few years ahead, leaving the next leap year (2020)
out of this challenge.

We will revisit this in an intermediate challenge. Have fun! '''

'''
TEST CODE:

import datetime
from itertools import islice

from gendates import gen_special_pybites_dates


def test_gen_special_pybites_dates():
    gen = gen_special_pybites_dates()
    dates = list(islice(gen, 100))

    expected = [datetime.datetime(2017, 3, 29, 0, 0),    1
                datetime.datetime(2017, 7, 7, 0, 0),     2
                datetime.datetime(2017, 10, 15, 0, 0),   3
                datetime.datetime(2017, 12, 19, 0, 0),   0
                datetime.datetime(2018, 1, 23, 0, 0),    1
                datetime.datetime(2018, 5, 3, 0, 0),     2
                datetime.datetime(2018, 8, 11, 0, 0),    3
                datetime.datetime(2018, 11, 19, 0, 0),   0 ----
                datetime.datetime(2018, 12, 19, 0, 0),   1
                datetime.datetime(2019, 2, 27, 0, 0)]    2

    assert dates[:10] == expected
'''

____ d__ _______ d__
____ d__ _______ t..
____ i.. _______ islice

PYBITES_BORN = d__ y.._2016,  m.._12,  d.._19)

___ gen_special_pybites_dates_1

    days = 0
    w... T...
        days += 1
        __ days % 100 __ 0 o. days % 365 __ 0:
            y.. PYBITES_BORN + t..(d.._days)

___ gen_special_pybites_dates_2

    plus365 = t..(d.._365)
    plus100 = t..(d.._100)
    next365 = PYBITES_BORN + plus365
    next100 = PYBITES_BORN + plus100
    w... T...
        __ next365 < next100:
            nextevent = next365
            next365 += plus365
        ____:
            nextevent = next100
            next100 += plus100
        y.. nextevent

gen = gen_special_pybites_dates()
dates = l..(islice(gen,20))
print(dates)

