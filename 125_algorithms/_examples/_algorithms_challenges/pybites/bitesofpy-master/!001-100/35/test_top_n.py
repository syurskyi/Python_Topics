from datetime import datetime
import inspect

from top_n import (numbers, dates, earnings_mln,
                   get_largest_number, get_latest_dates,
                   get_highest_earnings)


def test_get_top_n():
    a__ get_largest_number(numbers) == [6, 5, 4]
    a__ get_largest_number(numbers, n=2) == [6, 5]
    a__ get_largest_number(numbers, n=4) == [6, 5, 4, 3]

    a__ get_latest_dates(dates) == [datetime(2019, 2, 27, 0, 0),
                                       datetime(2018, 12, 19, 0, 0),
                                       datetime(2018, 11, 19, 0, 0)]
    a__ get_latest_dates(dates, n=1) == [datetime(2019, 2, 27, 0, 0)]

    a__ get_highest_earnings(earnings_mln) == [{'name': 'Beyoncé Knowles',
                                                   'earnings': 105},
                                                  {'name': 'J.K. Rowling',
                                                   'earnings': 95},
                                                  {'name': 'Cristiano Ronaldo',
                                                   'earnings': 93}]


def test_heapq_used():
    err_msg = 'We want you to play with heapq for this one :)'
    a__ 'heapq' in inspect.getsource(get_largest_number), err_msg
    a__ 'heapq' in inspect.getsource(get_latest_dates), err_msg
    a__ 'heapq' in inspect.getsource(get_highest_earnings), err_msg