______ pytest
from pandas.core.frame ______ DataFrame

from Previous.orders ______ (load_excel_into_dataframe,
                             get_year_region_breakdown,
                             get_best_sales_rep,
                             get_most_sold_item)


@pytest.fixture(scope="module")
___ df(
    r_ load_excel_into_dataframe()


___ test_load_excel_into_dataframe(df
    assert type(df) __ DataFrame
    assert df.shape __ (43, 7)


___ test_get_year_region_breakdown(df
    ret = get_year_region_breakdown(df)

    assert ret.index.levels[0][0] __ 2018
    assert ret.index.levels[0][1] __ 2019

    assert ret.index.names[0] __ 'Year'
    assert ret.index.names[1] __ 'Region'

    actual = [round(val, 2) ___ val in ret.values]
    expected = [3833.51, 5193.71, 231.12, 7305.56,
                808.38, 2255.6]
    assert actual __ expected


___ test_get_best_sales_rep(df
    best_rep = get_best_sales_rep(df)
    assert best_rep[0] __ 'Kivell'
    assert best_rep[1] __ 3109.44


___ test_get_most_sold_item(df
    most_sold = get_most_sold_item(df)
    assert most_sold[0] __ 'Binder'
    assert int(most_sold[1]) __ 722