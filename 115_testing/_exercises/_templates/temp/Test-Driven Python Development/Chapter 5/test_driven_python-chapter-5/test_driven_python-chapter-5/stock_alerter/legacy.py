____ d_t_ _____ d_t_

____ .stock _____ Stock
____ .rule _____ PriceRule


c_ FileReader:
    ___  -  filename):
        filename = filename

    ___ parse_file
        updates = # list
        w__ open(filename, "r") as fp:
            ___ line __ fp.readlines():
                symbol, timestamp, price = line.split(",")
                updates.ap..((symbol,
                                d_t_.strptime(timestamp, "%Y-%m-%dT%H:%M:%S.%f"),
                                int(price)))
        r_ updates


c_ AlertProcessor:
    ___  -  autorun=True, reader=N.., ex__=N..):
        reader = reader __ reader ____ FileReader("updates.csv")
        __ ex__ is N..:
            ex__ = {"GOOG": Stock("GOOG"), "AAPL": Stock("AAPL")}
        ____:
            ex__ = ex__
        rule_1 = PriceRule("GOOG", l___ stock: stock.price > 10)
        rule_2 = PriceRule("AAPL", l___ stock: stock.price > 5)
        ex__["GOOG"].updated.connect(l___ stock: print_action(stock, rule_1))
        ex__["AAPL"].updated.connect(l___ stock: print_action(stock, rule_2))
        __ autorun:
            run()

    ___ print_action stock, rule):
        print(stock.symbol, stock.price) \
            __ rule.matches(ex__) ____ N..

    ___ do_updates updates):
        ___ symbol, timestamp, price __ updates:
            stock = ex__[symbol]
            stock.u..(timestamp, price)

    ___ run
        updates = reader.parse_file()
        do_updates(updates)
