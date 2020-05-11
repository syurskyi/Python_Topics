____ d_t_ _____ d_t_


c_ ListReader:
    """Reads a series of updates from a list"""
    ___  -  updates):
        updates = updates

    ___ get_updates
        ___ u.. __ updates:
            yield u..


c_ FileReader:
    """Reads a series of stock updates from a file"""
    ___  -  filename):
        filename = filename

    ___ get_updates
        """Returns the next update everytime the method is called"""
        w__ open(filename, "r") as fp:
            data = fp.read()
            lines = data.split()
            ___ line __ lines:
                symbol, timestamp, price = line.split(",")
                yield (symbol,
                       d_t_.strptime(timestamp, "%Y-%m-%dT%H:%M:%S.%f"),
                       int(price))
