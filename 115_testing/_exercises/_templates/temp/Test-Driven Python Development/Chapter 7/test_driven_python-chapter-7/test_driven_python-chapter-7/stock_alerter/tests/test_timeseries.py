_____ u__
from datetime _____ datetime

from ..timeseries _____ TimeSeries


c_ TimeSeriesTestCase ?.?
    ___ assert_has_price_history price_list, series):
        for index, expected_price in enumerate(price_list):
            actual_price = series[index].value
            if actual_price != expected_price:
                raise failureException("Price index {0}: {1} != {2}".format(
                    index, expected_price, actual_price))


c_ TimeSeriesEqualityTest(TimeSeriesTestCase):
    ___ test_timeseries_price_history
        series = TimeSeries()
        series.update(datetime(2014, 3, 10), 5)
        series.update(datetime(2014, 3, 11), 15)
        assert_has_price_history([5, 15], series)
