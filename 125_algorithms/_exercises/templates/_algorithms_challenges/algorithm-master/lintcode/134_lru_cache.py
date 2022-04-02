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


c_ LRUCache:
    ___ - , capacity
        """
        :type capacity: int
        """
        cap = capacity
        nodes    # dict
        D = CacheNode(-1)
        d = CacheNode(-1)
        D.nxt = d
        d.pre = D

    ___ get  key
        """
        :type key: int
        :rtype: int
        """
        __ key n.. __ nodes:
            r.. -1

        _update(key)
        r.. nodes[key].val

    ___ s..  key, val
        """
        :type key: int
        :type val: int
        :rtype: void
        """
        __ cap <= 0:
            r..

        __ key __ nodes:
            _update(key, val)
            r..

        w.... l..(nodes) >= cap:
            _evict()

        _add(key, val)

    ___ _evict
        node = _pop_head()
        del nodes[node.key]

    ___ _update  key, val_ N..
        node = nodes[key]

        __ val:
            node.val = val

        node.unlink()
        _add_tail(node)

    ___ _add  key, val
        nodes[key] = CacheNode(key, val)
        _add_tail(nodes[key])

    ___ _pop_head
        node = D.nxt
        node.unlink()
        r.. node

    ___ _add_tail  node
        node.link(d.pre, d)


c_ CacheNode:
    ___ - , key, val=N.., pre=N.., nxt_ N..
        key = key
        val = val
        pre = pre
        nxt = nxt

    ___ link  pre, nxt
        pre = pre
        nxt = nxt
        pre.nxt = self
        nxt.pre = self

    ___ unlink
        pre.nxt = nxt
        nxt.pre = pre
        pre = nxt = N..
