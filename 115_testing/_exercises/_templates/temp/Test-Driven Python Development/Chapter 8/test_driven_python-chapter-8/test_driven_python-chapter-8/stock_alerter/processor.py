c_ Processor:
    ___  -  reader, exchange):
        reader = reader
        exchange = exchange

    ___ process
        for symbol, timestamp, price in reader.get_updates():
            stock = exchange[symbol]
            stock.update(timestamp, price)
