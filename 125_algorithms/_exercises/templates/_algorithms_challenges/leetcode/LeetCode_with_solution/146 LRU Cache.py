"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations:
get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it
should invalidate the least recently used item before inserting a new item.
"""
__author__ = 'Danyang'


c_ Node(object):
    ___ - , key, val):
        key = key
        val = val
        pre, next = N.., N..


c_ LRUCache(object):
    ___ - , capacity):
        cap = capacity
        map    # dict  # key to node
        head = N..
        tail = N..

    ___ get  key):
        __ key __ map:
            cur = map[key]
            _elevate(cur)
            r.. cur.val

        r.. -1

    ___ set  key, value):
        __ key __ map:
            cur = map[key]
            cur.val = value
            _elevate(cur)
        ____:
            cur = Node(key, value)
            map[key] = cur
            _appendleft(cur)

            __ l..(map) > cap:
                last = _pop()
                del map[last.key]

    # doubly linked-list operations only
    ___ _appendleft  cur):
        """Normal or initially empty"""
        __ n.. head a.. n.. tail:
            head = cur
            tail = cur
            r..

        head = head
        cur.next, cur.pre, head.pre = head, N.., cur
        head = cur

    ___ _pop
        """Normal or resulting empty"""
        last = tail
        __ head __ tail:
            head, tail = N.., N..
            r.. last

        pre = last.pre
        pre.next = N..
        tail = pre
        r.. last

    ___ _elevate  cur):
        """Head, Tail, Middle"""
        pre, nxt = cur.pre, cur.next
        __ n.. pre:
            r..
        ____ n.. nxt:
            ... tail __ cur
            _pop()
        ____:
            pre.next, nxt.pre = nxt, pre

        _appendleft(cur)


c_ LRUCache_TLE(object):
    ___ - , capacity):
        capacity = capacity
        q    # list  # order by key
        dic    # dict

    ___ get  key):
        __ key __ dic:
            q.remove(key)
            q.insert(0, key)
            r.. dic[key]
        ____:
            r.. -1

    ___ set  key, value):
        """
        Algorithm:
        data structure: Queue and HashMap

        :param key: int
        :param value: int
        :return: value
        """
        __ key __ dic:
            q.remove(key)
            q.insert(0, key)
        ____:
            __ l..(q)+1 <= capacity:
                q.insert(0, key)
            ____:
                dic.pop(q.pop())
                q.insert(0, key)

        dic[key] = value
