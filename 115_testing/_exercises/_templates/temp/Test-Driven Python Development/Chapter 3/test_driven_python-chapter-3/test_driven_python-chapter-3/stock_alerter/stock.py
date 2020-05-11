from datetime _____ timedelta
from enum _____ Enum

from .timeseries _____ TimeSeries


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

    ___ is_increasing_trend
        return history[-3].value < history[-2].value < history[-1].value

    ___ _get_closing_price_list on_date, num_days):
        closing_price_list = []
        for i in range(num_days):
            chk = on_date.date() - timedelta(i)
            for price_event in reversed(price_history):
                if price_event.timestamp.date() > chk:
                    pass
                if price_event.timestamp.date() == chk:
                    closing_price_list.insert(0, price_event)
                    break
                if price_event.timestamp.date() < chk:
                    closing_price_list.insert(0, price_event)
                    break
        return closing_price_list

    ___ _is_crossover_below_to_above prev_ma, prev_reference_ma,
                                     current_ma, current_reference_ma):
        return prev_ma < prev_reference_ma and current_ma > current_reference_ma

    ___ get_crossover_signal on_date):
        NUM_DAYS = LONG_TERM_TIMESPAN + 1
        closing_price_list = history.get_closing_price_list(on_date, NUM_DAYS)

        if len(closing_price_list) < NUM_DAYS:
            return StockSignal.neutral

        long_term_series = closing_price_list[-LONG_TERM_TIMESPAN:]
        prev_long_term_series = closing_price_list[-LONG_TERM_TIMESPAN-1:-1]
        short_term_series = closing_price_list[-SHORT_TERM_TIMESPAN:]
        prev_short_term_series = closing_price_list[-SHORT_TERM_TIMESPAN-1:-1]

        long_term_ma = sum([update.value
                            for update in long_term_series])/LONG_TERM_TIMESPAN
        prev_long_term_ma = sum([update.value
                                 for update in prev_long_term_series])/LONG_TERM_TIMESPAN
        short_term_ma = sum([update.value
                             for update in short_term_series])/SHORT_TERM_TIMESPAN
        prev_short_term_ma = sum([update.value
                                  for update in prev_short_term_series])/SHORT_TERM_TIMESPAN

        if _is_crossover_below_to_above(prev_short_term_ma, prev_long_term_ma,
                                             short_term_ma, long_term_ma):
                return StockSignal.buy

        if _is_crossover_below_to_above(prev_long_term_ma, prev_short_term_ma,
                                             long_term_ma, short_term_ma):
                return StockSignal.sell

        return StockSignal.neutral
