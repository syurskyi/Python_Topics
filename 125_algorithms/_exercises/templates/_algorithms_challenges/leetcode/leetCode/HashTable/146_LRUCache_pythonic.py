#! /usr/bin/env python
# -*- coding: utf-8 -*-
import collections


c.. LRUCache:
    ___ __init__  capacity
        self.capacity = capacity
        # An OrderedDict is a dictionary subclass
        # that remembers the order in which its contents are added.
        self.cache = collections.OrderedDict()

    ___ get  key
        __ key n.. __ self.cache:
            r_ -1
        value = self.cache.pop(key)
        self.cache[key] = value
        r_ value

    ___ s..  key, value
        __ key __ self.cache:
            self.cache.pop(key)
        ____ l..(self.cache) __ self.capacity:
            self.cache.popitem(last=False)
        ____
            pass
        self.cache[key] = value

"""
if __name__ == '__main__':
    ca = LRUCache(2)
    ca.set(2, 1)
    print "AA", ca.get(2)
    ca.set(2, 2)
    print "BB",  ca.get(2)
    ca.set(3, 3)
    print "CC", ca.get(3)
    # what if: print "CC", ca.get(2)
    ca.set(4, 1)
    print "CC", ca.get(2)
"""
