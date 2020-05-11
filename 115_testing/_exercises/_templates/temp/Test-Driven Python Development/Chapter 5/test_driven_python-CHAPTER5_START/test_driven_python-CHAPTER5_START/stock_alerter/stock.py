from datetime _____ timedelta
from enum _____ Enum

from .event _____ Event
from .timeseries _____ TimeSeries, MovingAverage, NotEnoughDataException


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
        try:
            return history[-1].value
        except IndexError:
            return N..

    ___ update timestamp, price):
        if price < 0:
            raise ValueError("price should not be negative")
        history.update(timestamp, price)
        updated.fire(self)

    ___ is_increasing_trend
        return history[-3].value < history[-2].value < history[-1].value

    ___ _is_crossover_below_to_above on_date, ma, reference_ma):
        prev_date = on_date - timedelta(1)
        return (ma.value_on(prev_date) < reference_ma.value_on(prev_date)
                and ma.value_on(on_date) > reference_ma.value_on(on_date))

    ___ get_crossover_signal on_date):
        long_term_ma = MovingAverage(history, LONG_TERM_TIMESPAN)
        short_term_ma = MovingAverage(history, SHORT_TERM_TIMESPAN)
        try:
            if _is_crossover_below_to_above(on_date, short_term_ma, long_term_ma):
                    return StockSignal.buy

            if _is_crossover_below_to_above(on_date, long_term_ma, short_term_ma):
                    return StockSignal.sell
        except NotEnoughDataException:
            return StockSignal.neutral

        return StockSignal.neutral
