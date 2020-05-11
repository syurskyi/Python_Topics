from datetime _____ datetime

from .stock _____ Stock
from .rule _____ PriceRule


c_ AlertProcessor:
    ___  -
        exchange = {"GOOG": Stock("GOOG"), "AAPL": Stock("AAPL")}
        rule_1 = PriceRule("GOOG", lambda stock: stock.price > 10)
        rule_2 = PriceRule("AAPL", lambda stock: stock.price > 5)
        exchange["GOOG"].updated.connect(
            lambda stock: print(stock.symbol, stock.price) \
                          if rule_1.matches(exchange) else N..)
        exchange["AAPL"].updated.connect(
            lambda stock: print(stock.symbol, stock.price) \
                          if rule_2.matches(exchange) else N..)
        updates = []
        with open("updates.csv", "r") as fp:
            for line in fp.readlines():
                symbol, timestamp, price = line.split(",")
                updates.append((symbol,
                       datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S.%f"),
                       int(price)))
        for symbol, timestamp, price in updates:
            stock = exchange[symbol]
            stock.update(timestamp, price)
