import pytest
from pandas.core.frame import DataFrame

from Previous.orders import (load_excel_into_dataframe,
                             get_year_region_breakdown,
                             get_best_sales_rep,
                             get_most_sold_item)


@pytest.fixture(scope="module")
def df():
    return load_excel_into_dataframe()


def test_load_excel_into_dataframe(df):
    a__ type(df) == DataFrame
    a__ df.shape == (43, 7)


def test_get_year_region_breakdown(df):
    ret = get_year_region_breakdown(df)

    a__ ret.index.levels[0][0] == 2018
    a__ ret.index.levels[0][1] == 2019

    a__ ret.index.names[0] == 'Year'
    a__ ret.index.names[1] == 'Region'

    actual = [round(val, 2) for val in ret.values]
    expected = [3833.51, 5193.71, 231.12, 7305.56,
                808.38, 2255.6]
    a__ actual == expected


def test_get_best_sales_rep(df):
    best_rep = get_best_sales_rep(df)
    a__ best_rep[0] == 'Kivell'
    a__ best_rep[1] == 3109.44


def test_get_most_sold_item(df):
    most_sold = get_most_sold_item(df)
    a__ most_sold[0] == 'Binder'
    a__ int(most_sold[1]) == 722