'''
Created on Apr 23, 2017

@author: MT
'''

class Node(object):
    ___ __init__(self, key, val):
        self.val = val
        self.next = None
        self.prev = None
        self.freq = 1
        self.key = key

class LFUCache(object):

    ___ __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.hashmap = {}
        self.freqMap = {}
        self.length = 0
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.head.freq = float('-inf')
        self.tail.freq = float('inf')
    
    ___ get(self, key):
        """
        :type key: int
        :rtype: int
        """
        __ key not in self.hashmap:
            return -1
        else:
            value = self.hashmap[key].val
            self.updateNode(self.hashmap[key])
            return value
    
    ___ put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        __ self.capacity == 0:
            return
        __ key in self.hashmap:
            self.hashmap[key].val = value
            self.updateNode(self.hashmap[key])
        else:
            __ self.capacity > self.length:
                self.length += 1
                node = Node(key, value)
                self.hashmap[key] = node
                node.freq = 1
                __ 1 in self.freqMap:
                    tmp = self.freqMap[1][1] # tail of freq
                    nextNode = tmp.next
                    tmp.next = node
                    node.prev = tmp
                    node.next = nextNode
                    node.next.prev = node
                    self.freqMap[1][1] = node
                else:
                    nextNode = self.head.next
                    node.next = nextNode
                    node.prev = self.head
                    nextNode.prev = node
                    self.head.next = node
                    self.freqMap[1] = [node, node]
            else:
                node = Node(key, value)
                self.hashmap[key] = node
                firstNode = self.head.next
                freq = firstNode.freq
                __ self.freqMap[freq][0] == self.freqMap[freq][1]:
                    self.head.next = firstNode.next
                    firstNode.next.prev = self.head
                    del self.freqMap[freq]
                else:
                    self.freqMap[freq][0] = self.freqMap[freq][0].next
                    self.head.next = firstNode.next
                    firstNode.next.prev = self.head
                del self.hashmap[firstNode.key]
                __ 1 in self.freqMap:
                    tmp = self.freqMap[1][1] # tail of freq
                    nextNode = tmp.next
                    tmp.next = node
                    node.prev = tmp
                    node.next = nextNode
                    node.next.prev = node
                    self.freqMap[1][1] = node
                else:
                    nextNode = self.head.next
                    nextNode.prev = node
                    node.next = nextNode
                    self.head.next = node
                    node.prev = self.head
                    self.freqMap[1] = [node, node]
    
    ___ updateNode(self, node):
        freq = node.freq
        nextNode = self.freqMap[freq][1].next
        node.prev.next = node.next
        node.next.prev = node.prev
        __ self.freqMap[freq][0] == self.freqMap[freq][1]:
            del self.freqMap[freq]
        else:
            __ self.freqMap[freq][0] == node:
                self.freqMap[freq][0] = node.next
            __ self.freqMap[freq][1] == node:
                self.freqMap[freq][1] = node.prev
        node.freq += 1
        freq += 1
        __ freq in self.freqMap:
            tail = self.freqMap[freq][1]
            node.next = tail.next
            tail.next = node
            node.next.prev = node
            node.prev = tail
            self.freqMap[freq][1] = node
        else:
            prevNode = nextNode.prev
            prevNode.next = node
            node.next = nextNode
            nextNode.prev = node
            node.prev = prevNode
            self.freqMap[freq] = [node, node]
