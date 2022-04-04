#!/usr/bin/python3
"""
Design and implement a data structure for Least Frequently Used (LFU) cache. It
should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists
in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present.
When the cache reaches its capacity, it should invalidate the least frequently
used item before inserting a new item. For the purpose of this problem, when
there is a tie (i.e., two or more keys that have the same frequency), the least
recently used key would be evicted.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LFUCache cache = new LFUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.get(3);       // returns 3.
cache.put(4, 4);    // evicts key 1.
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""
____ c.. _______ d.., OrderedDict
DUMMY = N..


c_ LFUCache:

    ___ - , capacity: i..
        """
        Need priority queue (pq) to keep contract of frequency

        LRU: doubly linked list and map
        Sift up and sift down?

        Ordereded Dict
        map: key -> value
        map: key -> frequency
        map: frequency -> OrderededDict[keys]

        min count is +1
        """
        cap = capacity
        values    # dict
        freqs = d..(i..)
        keys = d..(OrderedDict)
        mini = -1  # mini frequency

    ___ get  key: i..) __ i..:
        __ key __ values:
            val = values[key]
            freq_org = freqs[key]
            freqs[key] += 1
            del keys[freq_org][key]
            keys[freq_org + 1][key] = DUMMY  # dummy

            __ freq_org __ mini a.. l..(keys[mini]) __ 0:
                mini = freq_org + 1

            r.. val
        ____:
            r.. - 1

    ___ put  key: i.., value: i..) __ N..
        __ cap __ 0:  # trivial
            r..

        __ key __ values:
            values[key] = value
            g.. key)  # update
        ____:
            __ l..(values) >= cap:
                evit_key, _ = keys[mini].popitem(last=F..)  # least recent is at head
                del values[evit_key]
                del freqs[evit_key]

            values[key] = value
            freqs[key] = 0
            keys[0][key] = DUMMY
            g.. key)  # update
            mini = 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
