____ gold _______ gold_prices, years_gold_value_decreased


___ test_gold_prices_full_data_set
    actual  years_gold_value_decreased()
    expected  (2013, 2009)
    ... actual __ expected


___ test_gold_prices_1950_1999
    data  '\n'.j..(gold_prices.s...s.. [:10])
    actual  years_gold_value_decreased(data)
    expected  (1981, 1979)
    ... actual __ expected


___ test_gold_prices_till_1980_1989
    data  '\n'.j..(gold_prices.s...s.. [-8:-6])
    actual  years_gold_value_decreased(data)
    expected  (1981, 1987)
    ... actual __ expected