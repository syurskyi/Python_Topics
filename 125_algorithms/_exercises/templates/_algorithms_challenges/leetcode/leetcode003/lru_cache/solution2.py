"""
Design and implement a data structure for Least Recently Used (LRU) cache. It
should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key
exists in the cache, otherwise return -1.

set(key, value) - Set or insert the value if the key is not already present.
When the cache reached its capacity, it should invalidate the least recently
used item before inserting a new item.

"""


class LRUCache(object):
    ___ __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.times = List()
        self.cache = {}

    ___ get(self, key):
        """
        :rtype: int
        """
        __ key __ self.cache:
            node = self.cache[key]
            self.times.touch(node)
            r.. node.value
        r.. -1

    ___ set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        __ key __ self.cache:
            node = self.cache[key]
            node.value = value
            self.times.touch(node)
        ____:
            __ self.times.size >= self.capacity:
                tail_node = self.times.tail
                self.times.remove(tail_node)
                del self.cache[tail_node.key]
            node = ListNode(key, value)
            self.cache[key] = node
            # Insert node with key to the head
            self.times.insert(node)


class ListNode(object):
    """Doubly Linked List node"""
    ___ __init__(self, key, value):
        self.prev = N..
        self.next = N..
        self.key = key
        self.value = value


class List(object):
    ___ __init__(self):
        self.head = N..
        self.tail = N..
        self.size = 0

    ___ insert(self, node):
        """Insert node to the head"""
        node.next = self.head
        __ self.head __ n.. N..
            self.head.prev = node
        ____:
            self.tail = node
        self.head = node
        self.size += 1

    ___ touch(self, node):
        """Move node to the head"""
        prev_node = node.prev
        next_node = node.next
        __ prev_node __ n.. N..
            prev_node.next = next_node
            __ next_node __ n.. N..
                next_node.prev = prev_node
            ____:
                self.tail = prev_node
            node.prev = N..
            node.next = self.head
            self.head.prev = node
            self.head = node

    ___ remove(self, node):
        """Remove a node"""
        prev_node = node.prev
        next_node = node.next
        # If node is not the head node
        __ prev_node __ n.. N..
            prev_node.next = next_node
            # If node is not the tail node
            __ next_node __ n.. N..
                next_node.prev = prev_node
            ____:
                self.tail = prev_node
        ____:
            self.head = N..
            self.tail = N..
        self.size -= 1
