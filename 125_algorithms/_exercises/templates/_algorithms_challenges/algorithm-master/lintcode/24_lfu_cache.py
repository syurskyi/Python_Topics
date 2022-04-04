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


c_ LFUCache:
    ___ - , capacity
        """
        :type capacity: int
        """
        cap = capacity
        nodes    # dict
        D = FreqNode(-1)
        d = FreqNode(-1)
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
        __ cap <_ 0:
            r..

        __ key __ nodes:
            _update(key, val)
            r..

        w.... l..(nodes) >_ cap:
            _evict()

        _add(key, val)

    ___ _evict
        freq_head = D.nxt
        cache_node = freq_head.pop_head()
        del nodes[cache_node.key]

        __ freq_head.is_empty
            freq_head.unlink()

    ___ _update  key, val_ N..
        cache_node = nodes[key]

        __ val:
            cache_node.val = val

        from_freq = cache_node.freq_node
        to_freq = N..

        __ from_freq.nxt a.. from_freq.nxt.freq __ from_freq.freq + 1:
            to_freq = from_freq.nxt
        ____
            to_freq = FreqNode(from_freq.freq + 1)
            from_freq.after(to_freq)

        cache_node.unlink()
        to_freq.append_tail(cache_node)

        __ from_freq.is_empty
            from_freq.unlink()

    ___ _add  key, val
        cache_node = CacheNode(key, val)
        nodes[key] = cache_node

        freq_head = D.nxt
        __ freq_head a.. freq_head.freq __ 0:
            freq_head.append_tail(cache_node)
            r..

        freq_head = FreqNode(0)
        freq_head.append_tail(cache_node)
        D.after(freq_head)


c_ CacheNode:
    ___ - , key, val=N.., freq_node=N.., pre=N.., nxt_ N..
        key = key
        val = val
        freq_node = freq_node
        pre = pre
        nxt = nxt

    # to change self in cache nodes
    ___ unlink
        pre.nxt = nxt
        nxt.pre = pre
        freq_node = pre = nxt = N..


c_ FreqNode:
    ___ - , freq, pre=N.., nxt_ N..
        freq = freq
        pre = pre
        nxt = nxt
        D = CacheNode(-1)
        d = CacheNode(-1)
        D.nxt = d
        d.pre = D

    # to change self in freq nodes
    ___ unlink
        pre.nxt = nxt
        nxt.pre = pre
        pre = nxt = D = d = N..

    # to change self in freq nodes
    ___ after  freq_node
        freq_node.pre = self
        freq_node.nxt = nxt
        nxt.pre = freq_node
        nxt = freq_node

    # to manage cache nodes
    ___ is_empty
        r.. D.nxt __ d

    # to manage cache nodes
    ___ pop_head
        __ is_empty
            r..

        head = D.nxt
        head.unlink()
        r.. head

    # to manage cache nodes
    ___ append_tail  cache_node
        cache_node.freq_node = self
        cache_node.pre = d.pre
        cache_node.nxt = d
        d.pre.nxt = cache_node
        d.pre = cache_node
