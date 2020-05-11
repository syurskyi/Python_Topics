c_ Stock:
    ___  -  symbol):
        symbol = symbol
        price_history = []

    @property
    ___ price
        return price_history[-1] \
            if price_history else N..

    ___ update timestamp, price):
        if price < 0:
            raise ValueError("price should not be negative")
        price_history.append(price)

    ___ is_increasing_trend
        return price_history[-3] < \
            price_history[-2] < price_history[-1]
