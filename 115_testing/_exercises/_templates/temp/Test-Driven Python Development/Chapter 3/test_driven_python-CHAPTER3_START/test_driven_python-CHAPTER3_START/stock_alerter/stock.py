_____ bisect
_____ collections
from datetime _____ timedelta

PriceEvent = collections.namedtuple("PriceEvent", ["timestamp", "price"])


c_ Stock:
    ___  -  symbol):
        symbol = symbol
        price_history = []

    @property
    ___ price
        return price_history[-1].price \
            if price_history else N..

    ___ update timestamp, price):
        if price < 0:
            raise ValueError("price should not be negative")
        bisect.insort_left(price_history, PriceEvent(timestamp, price))

    ___ is_increasing_trend
        return price_history[-3].price < \
            price_history[-2].price < price_history[-1].price

    ___ get_crossover_signal on_date):
        cpl = []
        for i in range(11):
            chk = on_date.date() - timedelta(i)
            for price_event in reversed(price_history):
                if price_event.timestamp.date() > chk:
                    pass
                if price_event.timestamp.date() == chk:
                    cpl.insert(0, price_event)
                    break
                if price_event.timestamp.date() < chk:
                    cpl.insert(0, price_event)
                    break

        # Return NEUTRAL signal
        if len(cpl) < 11:
            return 0

        # BUY signal
        if sum([update.price for update in cpl[-11:-1]])/10 \
                > sum([update.price for update in cpl[-6:-1]])/5 \
            and sum([update.price for update in cpl[-10:]])/10 \
                < sum([update.price for update in cpl[-5:]])/5:
                    return 1

        # BUY signal
        if sum([update.price for update in cpl[-11:-1]])/10 \
                < sum([update.price for update in cpl[-6:-1]])/5 \
            and sum([update.price for update in cpl[-10:]])/10 \
                > sum([update.price for update in cpl[-5:]])/5:
                    return -1

        # NEUTRAL signal
        return 0
