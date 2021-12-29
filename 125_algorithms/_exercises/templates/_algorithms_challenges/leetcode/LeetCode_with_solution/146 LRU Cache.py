"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations:
get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it
should invalidate the least recently used item before inserting a new item.
"""
__author__ = 'Danyang'


class Node(object):
    ___ __init__(self, key, val):
        self.key = key
        self.val = val
        self.pre, self.next = N.., N..


class LRUCache(object):
    ___ __init__(self, capacity):
        self.cap = capacity
        self.map = {}  # key to node
        self.head = N..
        self.tail = N..

    ___ get(self, key):
        __ key __ self.map:
            cur = self.map[key]
            self._elevate(cur)
            r.. cur.val

        r.. -1

    ___ set(self, key, value):
        __ key __ self.map:
            cur = self.map[key]
            cur.val = value
            self._elevate(cur)
        ____:
            cur = Node(key, value)
            self.map[key] = cur
            self._appendleft(cur)

            __ l..(self.map) > self.cap:
                last = self._pop()
                del self.map[last.key]

    # doubly linked-list operations only
    ___ _appendleft(self, cur):
        """Normal or initially empty"""
        __ n.. self.head a.. n.. self.tail:
            self.head = cur
            self.tail = cur
            r..

        head = self.head
        cur.next, cur.pre, head.pre = head, N.., cur
        self.head = cur

    ___ _pop(self):
        """Normal or resulting empty"""
        last = self.tail
        __ self.head __ self.tail:
            self.head, self.tail = N.., N..
            r.. last

        pre = last.pre
        pre.next = N..
        self.tail = pre
        r.. last

    ___ _elevate(self, cur):
        """Head, Tail, Middle"""
        pre, nxt = cur.pre, cur.next
        __ n.. pre:
            r..
        ____ n.. nxt:
            ... self.tail __ cur
            self._pop()
        ____:
            pre.next, nxt.pre = nxt, pre

        self._appendleft(cur)


class LRUCache_TLE(object):
    ___ __init__(self, capacity):
        self.capacity = capacity
        self.q    # list  # order by key
        self.dic = {}

    ___ get(self, key):
        __ key __ self.dic:
            self.q.remove(key)
            self.q.insert(0, key)
            r.. self.dic[key]
        ____:
            r.. -1

    ___ set(self, key, value):
        """
        Algorithm:
        data structure: Queue and HashMap

        :param key: int
        :param value: int
        :return: value
        """
        __ key __ self.dic:
            self.q.remove(key)
            self.q.insert(0, key)
        ____:
            __ l..(self.q)+1 <= self.capacity:
                self.q.insert(0, key)
            ____:
                self.dic.pop(self.q.pop())
                self.q.insert(0, key)

        self.dic[key] = value
