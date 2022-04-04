#!/usr/bin/python3
"""
Design and implement a data structure for Least Recently Used (LRU) cache. It
should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists
in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present.
When the cache reached its capacity, it should invalidate the least recently
used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""


c_ Node:
    ___ - , key, val
        key = key
        val = val
        prev, next = N.., N..


c_ LRUCache:

    ___ - , capacity: i..
        """
        O(1) look up - Map
        O(1) update most recent vs. least recent - Linked List
        But Single linked list is not enough then Double Linked List

        Need dummy head and tail to avoid over complication of null checking

        Essentially it is the OrderedDict
        """
        head = Node(N.., N..)
        tail = Node(N.., N..)
        head.next = tail
        tail.prev = head
        cap = capacity
        map    # dict

    ___ get  key: i..) __ i..:
        __ key __ map:
            node = map[key]
            _remove(key)
            _appendleft(node)
            r.. node.val

        r.. -1

    ___ put  key: i.., value: i..) __ N..
        __ key __ map:
            _remove(key)
        ____ l.. m..) >_ cap:
            node = tail.prev
            _remove(node.key)

        node = Node(key, value)
        _appendleft(node)

    ___ _appendleft  node: Node
        map[node.key] = node  # update/delete map in these two operators
        nxt = head.next
        head.next = node
        node.prev = head
        node.next = nxt
        nxt.prev = node

    ___ _remove  key: i..
        node = map[key]
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
        del map[key]  # update/delete map in these two operators

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
