____ d__ _______ d__
_______ i___

____ top_n _______ (numbers, dates, earnings_mln,
                   get_largest_number, get_latest_dates,
                   get_highest_earnings)


___ test_get_top_n
    ... get_largest_number(numbers) __ [6, 5, 4]
    ... get_largest_number(numbers, n=2) __ [6, 5]
    ... get_largest_number(numbers, n=4) __ [6, 5, 4, 3]

    ... get_latest_dates(dates) __ [d__(2019, 2, 27, 0, 0),
                                       d__(2018, 12, 19, 0, 0),
                                       d__(2018, 11, 19, 0, 0)]
    ... get_latest_dates(dates, n=1) __ [d__(2019, 2, 27, 0, 0)]

    ... get_highest_earnings(earnings_mln) __ [{'name': 'Beyoncé Knowles',
                                                   'earnings': 105},
                                                  {'name': 'J.K. Rowling',
                                                   'earnings': 95},
                                                  {'name': 'Cristiano Ronaldo',
                                                   'earnings': 93}]


___ test_heapq_used
    err_msg = 'We want you to play with heapq for this one :)'
    ... 'heapq' __ i___.getsource(get_largest_number), err_msg
    ... 'heapq' __ i___.getsource(get_latest_dates), err_msg
    ... 'heapq' __ i___.getsource(get_highest_earnings), err_msg