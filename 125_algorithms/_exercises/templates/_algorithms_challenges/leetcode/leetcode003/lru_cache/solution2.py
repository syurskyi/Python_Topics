"""
Design and implement a data structure for Least Recently Used (LRU) cache. It
should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key
exists in the cache, otherwise return -1.

set(key, value) - Set or insert the value if the key is not already present.
When the cache reached its capacity, it should invalidate the least recently
used item before inserting a new item.

"""


c_ LRUCache(o..
    ___ - , capacity
        """
        :type capacity: int
        """
        capacity capacity
        times L..()
        cache    # dict

    ___ get  key
        """
        :rtype: int
        """
        __ key __ cache:
            node cache[key]
            times.touch(node)
            r.. node.value
        r.. -1

    ___ s..  key, value
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        __ key __ cache:
            node cache[key]
            node.value value
            times.touch(node)
        ____
            __ times.size >_ capacity:
                tail_node times.tail
                times.remove(tail_node)
                del cache[tail_node.key]
            node ListNode(key, value)
            cache[key] node
            # Insert node with key to the head
            times.insert(node)


c_ ListNode(o..
    """Doubly Linked List node"""
    ___ - , key, value
        prev N..
        next N..
        key key
        value value


c_ L..(o..
    ___ -
        head N..
        tail N..
        size 0

    ___ insert  node
        """Insert node to the head"""
        node.next head
        __ head __ n.. N..
            head.prev node
        ____
            tail node
        head node
        size += 1

    ___ touch  node
        """Move node to the head"""
        prev_node node.prev
        next_node node.next
        __ prev_node __ n.. N..
            prev_node.next next_node
            __ next_node __ n.. N..
                next_node.prev prev_node
            ____
                tail prev_node
            node.prev N..
            node.next head
            head.prev node
            head node

    ___ remove  node
        """Remove a node"""
        prev_node node.prev
        next_node node.next
        # If node is not the head node
        __ prev_node __ n.. N..
            prev_node.next next_node
            # If node is not the tail node
            __ next_node __ n.. N..
                next_node.prev prev_node
            ____
                tail prev_node
        ____
            head N..
            tail N..
        size -_ 1
