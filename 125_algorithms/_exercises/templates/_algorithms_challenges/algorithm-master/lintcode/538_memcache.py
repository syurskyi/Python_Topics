class Memcache:

    INT_MAX = 0x7FFFFFFF
    PERMANENT_TTL = -1
    storage = {}

    """
    @param: curtTime: An integer
    @param: key: An integer
    @return: An integer
    """
    ___ get(self, curtTime, key
        __ key not in self.storage:
            r_ self.INT_MAX

        __ (curtTime < self.storage[key]['expired_at'] or
            self.storage[key]['expired_at'] __ self.PERMANENT_TTL
            r_ self.storage[key]['val']

        r_ self.INT_MAX

    """
    @param: curtTime: An integer
    @param: key: An integer
    @param: value: An integer
    @param: ttl: An integer
    @return: nothing
    """
    ___ set(self, curtTime, key, value, ttl
        __ ttl > 0:
            self.storage[key] = self._new_item(key, value, curtTime + ttl)
        ____
            self.storage[key] = self._new_item(key, value, self.PERMANENT_TTL)

    """
    @param: curtTime: An integer
    @param: key: An integer
    @return: nothing
    """
    ___ delete(self, curtTime, key
        __ key in self.storage:
            del self.storage[key]

    """
    @param: curtTime: An integer
    @param: key: An integer
    @param: delta: An integer
    @return: An integer
    """
    ___ incr(self, curtTime, key, delta
        __ key not in self.storage:
            r_ self.INT_MAX

        __ (curtTime < self.storage[key]['expired_at'] or
            self.storage[key]['expired_at'] __ self.PERMANENT_TTL
            self.storage[key]['val'] += delta
            r_ self.storage[key]['val']

        r_ self.INT_MAX

    """
    @param: curtTime: An integer
    @param: key: An integer
    @param: delta: An integer
    @return: An integer
    """
    ___ decr(self, curtTime, key, delta
        r_ self.incr(curtTime, key, -1 * delta)

    ___ _new_item(self, key, value, expired_at
        r_ {
            'key': key,
            'val': value,
            'expired_at': expired_at
        }
