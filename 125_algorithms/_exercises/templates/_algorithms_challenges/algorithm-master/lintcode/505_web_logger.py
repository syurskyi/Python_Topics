class WebLogger:
    ___ __init__(self):
        dummy    # list
        dummy[:] = [dummy, dummy, -1]
        self.dummy = dummy
        self.size = 0

    """
    @param: timestamp: An integer
    @return: nothing
    """
    ___ hit(self, timestamp):
        tail = self.dummy[0]

        tail[1] = self.dummy[0] = _n = [N.., N.., timestamp]
        _n[0] = tail
        _n[1] = self.dummy

        self.size += 1

    """
    @param: timestamp: An integer
    @return: An integer
    """
    ___ get_hit_count_in_last_5_minutes(self, timestamp):
        head = self.dummy[1]

        while (head __ n.. self.dummy and
               head[2] + 300 <= timestamp):
            _, nxt, _ = head
            self.dummy[1] = nxt
            nxt[0] = self.dummy
            head[0] = head[1] = N..

            head = nxt
            self.size -= 1

        r.. self.size
