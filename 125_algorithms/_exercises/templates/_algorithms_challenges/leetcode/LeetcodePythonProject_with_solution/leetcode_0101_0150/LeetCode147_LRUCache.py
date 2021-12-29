'''
Created on Feb 9, 2017

@author: MT
'''

class Node(object):
    ___ __init__(self, key, val, prevNode=None, nextNode_ N..
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
        self.head = None
        self.tail = None
    
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
            else:
                prevNode.next = node
                node.prev = prevNode
        else:
            __ next:
                self.head = nextNode
                nextNode.prev = None
                self.tail.next = node
                node.prev = self.tail
            else:
                self.head = node
        self.tail = node
        self.head.prev = None
        self.tail.next = None
    
    ___ get(self, key):
        __ key not in self.map:
            return -1
        else:
            node = self.map[key]
            val = node.val
            self.removeAndAppend(key)
            return val
    
    ___ set(self, key, value):
        __ not self.map:
            node = Node(key, value)
            self.map[key] = node
            self.head = node
            self.tail = node
        else:
            __ key in self.map:
                self.removeAndAppend(key)
                self.tail.val = value
            else:
                __ len(self.map) < self.capacity:
                    node = Node(key, value)
                    self.tail.next = node
                    node.prev = self.tail
                    self.tail = node
                    self.map[key] = node
                elif len(self.map) == self.capacity:
                    node = Node(key, value)
                    self.map[key] = node
                    tmpHead = self.head
                    del self.map[tmpHead.key]
                    __ self.head.next:
                        self.head = self.head.next
                        self.head.prev = None
                        self.tail.next = node
                        node.prev = self.tail
                        self.tail = node
                    else:
                        self.head = node
                        self.tail = node

__ __name__ == '__main__':
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
