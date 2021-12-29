"""
Main Concept:

Dm <-> a <-> b <-> c <-> dm  |<- cache_list (dll)

1. if cache is updated (set/get)
    => move to the end of cache_list
2. if cache is full
    => evict the most left node in cache first,
       that is `a` in above diagram
    => add the new cache to the end of the cache_list as new tail
"""


class LRUCache:
    ___ __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.nodes = {}
        self.D = CacheNode(-1)
        self.d = CacheNode(-1)
        self.D.nxt = self.d
        self.d.pre = self.D

    ___ get(self, key):
        """
        :type key: int
        :rtype: int
        """
        __ key n.. __ self.nodes:
            r.. -1

        self._update(key)
        r.. self.nodes[key].val

    ___ set(self, key, val):
        """
        :type key: int
        :type val: int
        :rtype: void
        """
        __ self.cap <= 0:
            r..

        __ key __ self.nodes:
            self._update(key, val)
            r..

        w.... l..(self.nodes) >= self.cap:
            self._evict()

        self._add(key, val)

    ___ _evict(self):
        node = self._pop_head()
        del self.nodes[node.key]

    ___ _update(self, key, val_ N..
        node = self.nodes[key]

        __ val:
            node.val = val

        node.unlink()
        self._add_tail(node)

    ___ _add(self, key, val):
        self.nodes[key] = CacheNode(key, val)
        self._add_tail(self.nodes[key])

    ___ _pop_head(self):
        node = self.D.nxt
        node.unlink()
        r.. node

    ___ _add_tail(self, node):
        node.link(self.d.pre, self.d)


class CacheNode:
    ___ __init__(self, key, val=N.., pre=N.., nxt_ N..
        self.key = key
        self.val = val
        self.pre = pre
        self.nxt = nxt

    ___ link(self, pre, nxt):
        self.pre = pre
        self.nxt = nxt
        pre.nxt = self
        nxt.pre = self

    ___ unlink(self):
        self.pre.nxt = self.nxt
        self.nxt.pre = self.pre
        self.pre = self.nxt = N..
