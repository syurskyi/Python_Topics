"""
Design and implement a data structure for Least Recently Used (LRU) cache. It
should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key
exists in the cache, otherwise return -1.

set(key, value) - Set or insert the value if the key is not already present.
When the cache reached its capacity, it should invalidate the least recently
used item before inserting a new item.


TLE
"""


class LRUCache:

    # @param capacity, an integer
    ___ __init__(self, capacity
        self.capacity = capacity
        self.times = {}
        self.cache = {}
        self.timestamp = 0

    # @return an integer
    ___ get(self, key
        self.timestamp += 1
        __ key in self.cache:
            self.times[key] = self.timestamp
            r_ self.cache[key]
        r_ -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    ___ set(self, key, value
        self.timestamp += 1
        __ key in self.cache:
            self.times[key] = self.timestamp
        ____
            __ le.(self.cache) >= self.capacity:
                lru_key = self.get_lru_key()
                del self.cache[lru_key]
                del self.times[lru_key]
            self.cache[key] = value
            self.times[key] = self.timestamp

    ___ get_lru_key(self
        min_time = self.timestamp
        res = None
        ___ key in self.times:
            __ self.times[key] <= min_time:
                res = key
                min_time = self.times[key]
        r_ res
