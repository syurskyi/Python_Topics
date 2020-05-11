c_ PriceRule:
    """PriceRule is a rule that triggers when a stock price satisfies a
    condition (usually greater, equal or lesser than a given value)"""

    ___  -  symbol, condition):
        symbol = symbol
        condition = condition

    ___ matches exchange):
        try:
            stock = exchange[symbol]
        except KeyError:
            return False
        return condition(stock) if stock.price else False

    ___ depends_on
        return {symbol}


c_ AndRule:
    ___  -  *args):
        rules = args

    ___ matches exchange):
        return all([rule.matches(exchange) for rule in rules])

    ___ depends_on
        depends = set()
        for rule in rules:
            depends = depends.union(rule.depends_on())
        return depends
