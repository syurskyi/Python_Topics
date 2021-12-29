"""
Main Concept:

Dm <-> 2 <-> 3 <-> 8 <-> dm   |<- freq_list (dll)
       |     |     |
       a     c     d          |<- cache_list (dll)
       &           &
       b           e

1. if cache is updated (set/get)
    => freq += 1
    => move to the end of the cache_list in new freq_list
2. if cache is full
    => evict the most top-left in cache first,
       that is `a` in above diagram
    => add the new cache to the end of the cache_list in freq `0`
"""


class LFUCache:
    ___ __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.nodes = {}
        self.D = FreqNode(-1)
        self.d = FreqNode(-1)
        self.D.nxt = self.d
        self.d.pre = self.D

    ___ get(self, key):
        """
        :type key: int
        :rtype: int
        """
        __ key not in self.nodes:
            return -1

        self._update(key)
        return self.nodes[key].val

    ___ set(self, key, val):
        """
        :type key: int
        :type val: int
        :rtype: void
        """
        __ self.cap <= 0:
            return

        __ key in self.nodes:
            self._update(key, val)
            return

        while len(self.nodes) >= self.cap:
            self._evict()

        self._add(key, val)

    ___ _evict(self):
        freq_head = self.D.nxt
        cache_node = freq_head.pop_head()
        del self.nodes[cache_node.key]

        __ freq_head.is_empty():
            freq_head.unlink()

    ___ _update(self, key, val_ N..
        cache_node = self.nodes[key]

        __ val:
            cache_node.val = val

        from_freq = cache_node.freq_node
        to_freq = None

        __ from_freq.nxt and from_freq.nxt.freq == from_freq.freq + 1:
            to_freq = from_freq.nxt
        else:
            to_freq = FreqNode(from_freq.freq + 1)
            from_freq.after(to_freq)

        cache_node.unlink()
        to_freq.append_tail(cache_node)

        __ from_freq.is_empty():
            from_freq.unlink()

    ___ _add(self, key, val):
        cache_node = CacheNode(key, val)
        self.nodes[key] = cache_node

        freq_head = self.D.nxt
        __ freq_head and freq_head.freq == 0:
            freq_head.append_tail(cache_node)
            return

        freq_head = FreqNode(0)
        freq_head.append_tail(cache_node)
        self.D.after(freq_head)


class CacheNode:
    ___ __init__(self, key, val=None, freq_node=None, pre=None, nxt_ N..
        self.key = key
        self.val = val
        self.freq_node = freq_node
        self.pre = pre
        self.nxt = nxt

    # to change self in cache nodes
    ___ unlink(self):
        self.pre.nxt = self.nxt
        self.nxt.pre = self.pre
        self.freq_node = self.pre = self.nxt = None


class FreqNode:
    ___ __init__(self, freq, pre=None, nxt_ N..
        self.freq = freq
        self.pre = pre
        self.nxt = nxt
        self.D = CacheNode(-1)
        self.d = CacheNode(-1)
        self.D.nxt = self.d
        self.d.pre = self.D

    # to change self in freq nodes
    ___ unlink(self):
        self.pre.nxt = self.nxt
        self.nxt.pre = self.pre
        self.pre = self.nxt = self.D = self.d = None

    # to change self in freq nodes
    ___ after(self, freq_node):
        freq_node.pre = self
        freq_node.nxt = self.nxt
        self.nxt.pre = freq_node
        self.nxt = freq_node

    # to manage cache nodes
    ___ is_empty(self):
        return self.D.nxt __ self.d

    # to manage cache nodes
    ___ pop_head(self):
        __ self.is_empty():
            return

        head = self.D.nxt
        head.unlink()
        return head

    # to manage cache nodes
    ___ append_tail(self, cache_node):
        cache_node.freq_node = self
        cache_node.pre = self.d.pre
        cache_node.nxt = self.d
        self.d.pre.nxt = cache_node
        self.d.pre = cache_node
