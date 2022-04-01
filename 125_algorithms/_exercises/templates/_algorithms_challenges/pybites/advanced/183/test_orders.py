_______ p__
____ pandas.core.frame _______ DataFrame

____ orders _______ (load_excel_into_dataframe,
                    get_year_region_breakdown,
                    get_best_sales_rep,
                    get_most_sold_item)


@p__.f..(scope="module")
___ df
    r.. load_excel_into_dataframe()


___ test_load_excel_into_dataframe(df):
    ... t..(df) __ DataFrame
    ... df.shape __ (43, 7)


___ test_get_year_region_breakdown(df):
    ret = get_year_region_breakdown(df)

    ... ret.index.levels[0][0] __ 2018
    ... ret.index.levels[0][1] __ 2019

    ... ret.index.names[0] __ 'Year'
    ... ret.index.names[1] __ 'Region'

    actual = [r..(f__(val), 2) ___ val __ ret.values]
    expected = [3833.51, 5193.71, 231.12, 7305.56,
                808.38, 2255.6]
    ... actual __ expected


___ test_get_best_sales_rep(df):
    best_rep = get_best_sales_rep(df)
    ... best_rep[0] __ 'Kivell'
    ... best_rep[1] __ 3109.44


___ test_get_most_sold_item(df):
    most_sold = get_most_sold_item(df)
    ... most_sold[0] __ 'Binder'
    ... i..(most_sold[1]) __ 722