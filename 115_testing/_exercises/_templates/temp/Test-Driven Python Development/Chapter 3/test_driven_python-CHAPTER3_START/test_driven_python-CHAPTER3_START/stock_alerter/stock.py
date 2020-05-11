_____ bisect
_____ col..
____ d_t_ _____ timedelta

PriceEvent = col...namedtuple("PriceEvent", ["timestamp", "price"])


c_ Stock:
    ___  -  symbol):
        symbol = symbol
        price_history = []

    @property
    ___ price
        r_ price_history[-1].price \
            __ price_history ____ N..

    ___ u.. timestamp, price):
        __ price < 0:
            r.. V..("price should not be negative")
        bisect.insort_left(price_history, PriceEvent(timestamp, price))

    ___ is_increasing_trend
        r_ price_history[-3].price < \
            price_history[-2].price < price_history[-1].price

    ___ get_crossover_signal on_date):
        cpl = []
        ___ i __ ra..(11):
            chk = on_date.date() - timedelta(i)
            ___ price_event __ reversed(price_history):
                __ price_event.timestamp.date() > chk:
                    pass
                __ price_event.timestamp.date() == chk:
                    cpl.insert(0, price_event)
                    break
                __ price_event.timestamp.date() < chk:
                    cpl.insert(0, price_event)
                    break

        # Return NEUTRAL signal
        __ le.(cpl) < 11:
            r_ 0

        # BUY signal
        __ sum([u...price ___ u.. __ cpl[-11:-1]])/10 \
                > sum([u...price ___ u.. __ cpl[-6:-1]])/5 \
            and sum([u...price ___ u.. __ cpl[-10:]])/10 \
                < sum([u...price ___ u.. __ cpl[-5:]])/5:
                    r_ 1

        # BUY signal
        __ sum([u...price ___ u.. __ cpl[-11:-1]])/10 \
                < sum([u...price ___ u.. __ cpl[-6:-1]])/5 \
            and sum([u...price ___ u.. __ cpl[-10:]])/10 \
                > sum([u...price ___ u.. __ cpl[-5:]])/5:
                    r_ -1

        # NEUTRAL signal
        r_ 0
