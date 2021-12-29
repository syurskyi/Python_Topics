____ Previous.stocks _______ (_cap_str_to_mln_float,
                             get_stock_symbol_with_highest_cap,
                             get_industry_cap,
                             get_sectors_with_max_and_min_stocks)


___ test_cap_str_to_mln_float():
    ... _cap_str_to_mln_float('n/a') __ 0
    ... _cap_str_to_mln_float('$100.45M') __ 100.45
    ... _cap_str_to_mln_float('$20.9B') __ 20900


___ test_get_stock_symbol_with_highest_cap():
    ... get_stock_symbol_with_highest_cap() __ 'JNJ'


___ test_get_industry_cap():
    ... get_industry_cap("Business Services") __ 368853.27
    ... get_industry_cap("Real Estate Investment Trusts") __ 243295.36


___ test_get_sectors_with_max_and_min_stocks():
    ... get_sectors_with_max_and_min_stocks() __ ('Finance',
                                                     'Transportation')