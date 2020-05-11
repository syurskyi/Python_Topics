from datetime _____ datetime


c_ ListReader:
    """Reads a series of updates from a list"""
    ___  -  updates):
        updates = updates

    ___ get_updates
        for update in updates:
            yield update


c_ FileReader:
    """Reads a series of stock updates from a file"""
    ___  -  filename):
        filename = filename

    ___ get_updates
        """Returns the next update everytime the method is called"""
        with open(filename, "r") as fp:
            data = fp.read()
            lines = data.split()
            for line in lines:
                symbol, timestamp, price = line.split(",")
                yield (symbol,
                       datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S.%f"),
                       int(price))
