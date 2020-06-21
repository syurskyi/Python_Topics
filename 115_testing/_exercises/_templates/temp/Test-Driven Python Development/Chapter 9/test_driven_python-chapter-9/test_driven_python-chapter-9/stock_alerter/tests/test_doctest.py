_____ doctest
____ d_t_ _____ d_t_

____ stock_alerter _____ stock


___ setup_stock_doctest(doctest):
    s = stock.Stock("GOOG")
    doctest.globs.u..({"stock": s})


___ load_tests(loader, tests, pattern):
    tests.addTests(doctest.DocTestSuite(stock, globs={
        "datetime": d_t_,
        "Stock": stock.Stock
    }, setUp=setup_stock_doctest))
    options = doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE
    tests.addTests(doctest.DocFileSuite("readme.txt", package="stock_alerter", optionflags=options))
    r_ tests
