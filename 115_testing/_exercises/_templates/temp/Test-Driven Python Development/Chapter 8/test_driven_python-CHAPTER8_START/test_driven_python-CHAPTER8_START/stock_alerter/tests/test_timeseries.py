_____ u__
____ d_t_ _____ d_t_

____ ..timeseries _____ TimeSeries


c_ TimeSeriesTestCase ?.?
    ___ assert_has_price_history price_list, series):
        ___ index, expected_price __ enumerate(price_list):
            actual_price = series[index].value
            __ actual_price != expected_price:
                r.. failureException("Price index {0}: {1} != {2}".format(
                    index, expected_price, actual_price))


c_ TimeSeriesEqualityTest(TimeSeriesTestCase):
    ___ test_timeseries_price_history
        series = TimeSeries()
        series.u..(d_t_(2014, 3, 10), 5)
        series.u..(d_t_(2014, 3, 11), 15)
        assert_has_price_history([5, 15], series)
