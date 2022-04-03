_______ p__

____ months _______ calc_months_passed


___ test_same_date
    ... calc_months_passed(2018, 11, 1) __ 0


___ test_nine_days_later
    ... calc_months_passed(2018, 11, 10) __ 0


___ test_ten_days_later
    ... calc_months_passed(2018, 11, 11) __ 1


___ test_one_month_and_nine_days_later
    ... calc_months_passed(2018, 12, 10) __ 1


___ test_one_month_and_ten_day_later
    ... calc_months_passed(2018, 12, 11) __ 2


___ test_one_year_one_month_and_nine_days_later
    ... calc_months_passed(2019, 12, 10) __ 13


___ test_one_year_one_month_and_ten_days_later
    ... calc_months_passed(2019, 12, 11) __ 14


___ test_non_int_input_args
    w__ p__.r.. T..
        calc_months_passed('a', 10, 1)
    w__ p__.r.. T..
        calc_months_passed(2018, 'b', 1)
    w__ p__.r.. T..
        calc_months_passed(2018, 10, 'c')


___ test_out_of_dt_range_args
    w__ p__.r..(V...
        calc_months_passed(-1000, 11, 1)
    w__ p__.r..(V...
        calc_months_passed(2018, 13, 1)
    w__ p__.r..(V...
        calc_months_passed(2018, 11, 34)


___ test_new_date_in_past_raises_value_error
    w__ p__.r..(V...
        calc_months_passed(2018, 10, 1)
"""
"""