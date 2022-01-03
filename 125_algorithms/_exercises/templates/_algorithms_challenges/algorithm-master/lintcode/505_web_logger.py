c_ WebLogger:
    ___ - ):
        dummy    # list
        dummy[:] = [dummy, dummy, -1]
        dummy = dummy
        size = 0

    """
    @param: timestamp: An integer
    @return: nothing
    """
    ___ hit(self, timestamp):
        tail = dummy[0]

        tail[1] = dummy[0] = _n = [N.., N.., timestamp]
        _n[0] = tail
        _n[1] = dummy

        size += 1

    """
    @param: timestamp: An integer
    @return: An integer
    """
    ___ get_hit_count_in_last_5_minutes(self, timestamp):
        head = dummy[1]

        w.... (head __ n.. dummy a..
               head[2] + 300 <= timestamp):
            _, nxt, _ = head
            dummy[1] = nxt
            nxt[0] = dummy
            head[0] = head[1] = N..

            head = nxt
            size -= 1

        r.. size
