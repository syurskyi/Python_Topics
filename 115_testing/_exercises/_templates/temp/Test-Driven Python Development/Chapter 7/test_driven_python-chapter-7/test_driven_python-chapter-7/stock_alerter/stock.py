____ d_t_ _____ timedelta
____ enum _____ Enum

____ .event _____ Event
____ .timeseries _____ TimeSeries, MovingAverage, NotEnoughDataException


c_ StockSignal(Enum):
    buy = 1
    neutral = 0
    sell = -1


c_ Stock:
    LONG_TERM_TIMESPAN = 10
    SHORT_TERM_TIMESPAN = 5

    ___  -  symbol):
        symbol = symbol
        history = TimeSeries()
        updated = Event()

    @property
    ___ price
        """Returns the current price of the Stock

        >>> stock.update(datetime(2011, 10, 3), 10)
        >>> stock.price
        10

        The method will return the latest price by timestamp, so even if
        updates are out of order, it will return the latest one

        >>> stock = Stock("GOOG")
        >>> stock.update(datetime(2011, 10, 3), 10)

        Now, let us do an update with a date that is earlier than the previous
        one

        >>> stock.update(datetime(2011, 10, 2), 5)

        And the method still returns the latest price

        >>> stock.price
        10

        If there are no updates, then the method returns None

        >>> stock = Stock("GOOG")
        >>> print(stock.price)
        None
        """
        ___
            r_ history[-1].value
        _____ IndexError:
            r_ N..

    ___ u.. timestamp, price):
        """Updates the stock with the price at the given timestamp

        >>> stock.update(datetime(2014, 10, 2), 10)
        >>> stock.price
        10

        The method raises a ValueError exception if the price is negative

        >>> stock.update(datetime(2014, 10, 2), -1)
        Traceback (most recent call last):
            ...
        ValueError: price should not be negative
        """
        __ price < 0:
            r.. V..("price should not be negative")
        history.u..(timestamp, price)
        updated.fire(self)

    ___ is_increasing_trend
        """Returns True if the past three values have been strictly increasing

        Returns False if there have been less than three updates so far

        >>> stock.is_increasing_trend()
        False
        """
        ___
            r_ history[-3].value < history[-2].value < history[-1].value
        _____ IndexError:
            r_ F..

    ___ _is_crossover_below_to_above on_date, ma, reference_ma):
        prev_date = on_date - timedelta(1)
        r_ (ma.value_on(prev_date) < reference_ma.value_on(prev_date)
                and ma.value_on(on_date) > reference_ma.value_on(on_date))

    ___ get_crossover_signal on_date):
        long_term_ma = MovingAverage(history, LONG_TERM_TIMESPAN)
        short_term_ma = MovingAverage(history, SHORT_TERM_TIMESPAN)
        ___
            __ _is_crossover_below_to_above(on_date, short_term_ma, long_term_ma):
                    r_ StockSignal.buy

            __ _is_crossover_below_to_above(on_date, long_term_ma, short_term_ma):
                    r_ StockSignal.sell
        _____ NotEnoughDataException:
            r_ StockSignal.neutral

        r_ StockSignal.neutral
