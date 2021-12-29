'''
Created on Feb 9, 2017

@author: MT
'''

class Node(object):
    ___ __init__(self, key, val, prevNode=N.., nextNode_ N..
        self.key = key
        self.val = val
        self.prev = prevNode
        self.next = nextNode

class LRUCache(object):
    ___ __init__(self, capacity):
        """
        :type capacity: int
        """
        self.map = {}
        self.capacity = capacity
        self.head = N..
        self.tail = N..
    
    ___ removeAndAppend(self, key):
        node = self.map[key]
        prevNode = node.prev
        nextNode = node.next
        __ prevNode:
            prevNode.next = node.next
            __ nextNode:
                nextNode.prev = prevNode
                self.tail.next = node
                node.prev = self.tail
            ____:
                prevNode.next = node
                node.prev = prevNode
        ____:
            __ next:
                self.head = nextNode
                nextNode.prev = N..
                self.tail.next = node
                node.prev = self.tail
            ____:
                self.head = node
        self.tail = node
        self.head.prev = N..
        self.tail.next = N..
    
    ___ get(self, key):
        __ key n.. __ self.map:
            r.. -1
        ____:
            node = self.map[key]
            val = node.val
            self.removeAndAppend(key)
            r.. val
    
    ___ set(self, key, value):
        __ n.. self.map:
            node = Node(key, value)
            self.map[key] = node
            self.head = node
            self.tail = node
        ____:
            __ key __ self.map:
                self.removeAndAppend(key)
                self.tail.val = value
            ____:
                __ l..(self.map) < self.capacity:
                    node = Node(key, value)
                    self.tail.next = node
                    node.prev = self.tail
                    self.tail = node
                    self.map[key] = node
                ____ l..(self.map) __ self.capacity:
                    node = Node(key, value)
                    self.map[key] = node
                    tmpHead = self.head
                    del self.map[tmpHead.key]
                    __ self.head.next:
                        self.head = self.head.next
                        self.head.prev = N..
                        self.tail.next = node
                        node.prev = self.tail
                        self.tail = node
                    ____:
                        self.head = node
                        self.tail = node

__ __name__ __ '__main__':
    cache = LRUCache(2)
    cache.set(1, 1)
    cache.set(2, 2)
    print(cache.get(1))
    cache.set(3, 3)
    print(cache.get(2))
    cache.set(4, 4)
    print(cache.get(1))
    print(cache.get(3))
    print(cache.get(4))
