c_ PriceRule:
    """PriceRule is a rule that triggers when a stock price satisfies a
    condition (usually greater, equal or lesser than a given value)"""

    ___  -  symbol, condition):
        symbol = symbol
        condition = condition

    ___ matches ex__):
        ___
            stock = ex__[symbol]
        _____ K..
            r_ F..
        r_ condition(stock) __ stock.price ____ F..

    ___ depends_on
        r_ {symbol}


c_ AndRule:
    ___  -  *args):
        rules = args

    ___ matches ex__):
        r_ all([rule.m..(ex__) ___ rule __ rules])

    ___ depends_on
        depends = se.()
        ___ rule __ rules:
            depends = depends.union(rule.depends_on())
        r_ depends
