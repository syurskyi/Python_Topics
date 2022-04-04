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


c_ LRUCache:

    # @param capacity, an integer
    ___ - , capacity
        capacity = capacity
        times    # dict
        cache    # dict
        timestamp = 0

    # @return an integer
    ___ get  key
        timestamp += 1
        __ key __ cache:
            times[key] = timestamp
            r.. cache[key]
        r.. -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    ___ s..  key, value
        timestamp += 1
        __ key __ cache:
            times[key] = timestamp
        ____
            __ l..(cache) >= capacity:
                lru_key = get_lru_key()
                del cache[lru_key]
                del times[lru_key]
            cache[key] = value
            times[key] = timestamp

    ___ get_lru_key
        min_time = timestamp
        res = N..
        ___ key __ times:
            __ times[key] <= min_time:
                res = key
                min_time = times[key]
        r.. res
