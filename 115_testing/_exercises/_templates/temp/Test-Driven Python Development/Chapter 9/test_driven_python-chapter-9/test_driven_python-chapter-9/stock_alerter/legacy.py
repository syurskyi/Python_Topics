from datetime _____ datetime

from .stock _____ Stock
from .rule _____ PriceRule


c_ FileReader:
    ___  -  filename):
        filename = filename

    ___ parse_file
        updates = []
        with open(filename, "r") as fp:
            for line in fp.readlines():
                symbol, timestamp, price = line.split(",")
                updates.append((symbol,
                                datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S.%f"),
                                int(price)))
        return updates


c_ AlertProcessor:
    ___  -  autorun=True, reader=N.., exchange=N..):
        reader = reader if reader else FileReader("updates.csv")
        if exchange is N..:
            exchange = {"GOOG": Stock("GOOG"), "AAPL": Stock("AAPL")}
        else:
            exchange = exchange
        rule_1 = PriceRule("GOOG", lambda stock: stock.price > 10)
        rule_2 = PriceRule("AAPL", lambda stock: stock.price > 5)
        exchange["GOOG"].updated.connect(lambda stock: print_action(stock, rule_1))
        exchange["AAPL"].updated.connect(lambda stock: print_action(stock, rule_2))
        if autorun:
            run()

    ___ print_action stock, rule):
        print(stock.symbol, stock.price) \
            if rule.matches(exchange) else N..

    ___ do_updates updates):
        for symbol, timestamp, price in updates:
            stock = exchange[symbol]
            stock.update(timestamp, price)

    ___ run
        updates = reader.parse_file()
        do_updates(updates)
