class Memcache:

    INT_MAX = 0x7FFFFFFF
    PERMANENT_TTL = -1
    storage = {}

    """
    @param: curtTime: An integer
    @param: key: An integer
    @return: An integer
    """
    ___ get(self, curtTime, key):
        __ key n.. __ self.storage:
            r.. self.INT_MAX

        __ (curtTime < self.storage[key]['expired_at'] o.
            self.storage[key]['expired_at'] __ self.PERMANENT_TTL):
            r.. self.storage[key]['val']

        r.. self.INT_MAX

    """
    @param: curtTime: An integer
    @param: key: An integer
    @param: value: An integer
    @param: ttl: An integer
    @return: nothing
    """
    ___ set(self, curtTime, key, value, ttl):
        __ ttl > 0:
            self.storage[key] = self._new_item(key, value, curtTime + ttl)
        ____:
            self.storage[key] = self._new_item(key, value, self.PERMANENT_TTL)

    """
    @param: curtTime: An integer
    @param: key: An integer
    @return: nothing
    """
    ___ delete(self, curtTime, key):
        __ key __ self.storage:
            del self.storage[key]

    """
    @param: curtTime: An integer
    @param: key: An integer
    @param: delta: An integer
    @return: An integer
    """
    ___ incr(self, curtTime, key, delta):
        __ key n.. __ self.storage:
            r.. self.INT_MAX

        __ (curtTime < self.storage[key]['expired_at'] o.
            self.storage[key]['expired_at'] __ self.PERMANENT_TTL):
            self.storage[key]['val'] += delta
            r.. self.storage[key]['val']

        r.. self.INT_MAX

    """
    @param: curtTime: An integer
    @param: key: An integer
    @param: delta: An integer
    @return: An integer
    """
    ___ decr(self, curtTime, key, delta):
        r.. self.incr(curtTime, key, -1 * delta)

    ___ _new_item(self, key, value, expired_at):
        r.. {
            'key': key,
            'val': value,
            'expired_at': expired_at
        }
