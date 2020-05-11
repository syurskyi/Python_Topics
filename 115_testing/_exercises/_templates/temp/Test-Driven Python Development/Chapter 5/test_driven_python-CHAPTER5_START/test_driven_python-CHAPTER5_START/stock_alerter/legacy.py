____ d_t_ _____ d_t_

____ .stock _____ Stock
____ .rule _____ PriceRule


c_ AlertProcessor:
    ___  -
        ex__ = {"GOOG": Stock("GOOG"), "AAPL": Stock("AAPL")}
        rule_1 = PriceRule("GOOG", l___ stock: stock.price > 10)
        rule_2 = PriceRule("AAPL", l___ stock: stock.price > 5)
        ex__["GOOG"].updated.connect(
            l___ stock: print(stock.symbol, stock.price) \
                          __ rule_1.m..(ex__) ____ N..)
        ex__["AAPL"].updated.connect(
            l___ stock: print(stock.symbol, stock.price) \
                          __ rule_2.m..(ex__) ____ N..)
        updates = []
        w__ open("updates.csv", "r") as fp:
            ___ line __ fp.readlines():
                symbol, timestamp, price = line.split(",")
                updates.ap..((symbol,
                       d_t_.strptime(timestamp, "%Y-%m-%dT%H:%M:%S.%f"),
                       int(price)))
        ___ symbol, timestamp, price __ updates:
            stock = ex__[symbol]
            stock.u..(timestamp, price)
