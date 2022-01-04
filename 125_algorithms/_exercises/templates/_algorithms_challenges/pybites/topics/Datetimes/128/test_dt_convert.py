_______ pytest

____ dt_convert _______ years_ago, convert_eu_to_us_date


___ test_years_ago
    ... years_ago('8 Aug, 2015') __ 3
    ... years_ago('6 Sep, 2014') __ 4
    ... years_ago('1 Oct, 2010') __ 8
    ... years_ago('31 Dec, 1958') __ 60


___ test_years_ago_wrong_input
    with pytest.raises(ValueError):
        # Sept != valid %b value 'Sep'
        ... years_ago('6 Sept, 2014') __ 4


___ test_convert_eu_to_us_date
    ... convert_eu_to_us_date('11/03/2002') __ '03/11/2002'
    ... convert_eu_to_us_date('18/04/2008') __ '04/18/2008'
    ... convert_eu_to_us_date('12/12/2014') __ '12/12/2014'
    ... convert_eu_to_us_date('1/3/2004') __ '03/01/2004'


___ test_convert_eu_to_us_date_invalid_day
    with pytest.raises(ValueError):
        convert_eu_to_us_date('41/03/2002')


___ test_convert_eu_to_us_date_invalid_month
    with pytest.raises(ValueError):
        convert_eu_to_us_date('11/13/2002')


___ test_convert_eu_to_us_date_invalid_year
    with pytest.raises(ValueError):
        convert_eu_to_us_date('11/13/year') 