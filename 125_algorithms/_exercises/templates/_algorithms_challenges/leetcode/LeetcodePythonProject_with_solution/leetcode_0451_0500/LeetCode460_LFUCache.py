'''
Created on Apr 23, 2017

@author: MT
'''

c_ Node(o..):
    ___ - , key, val):
        val = val
        next = N..
        prev = N..
        freq = 1
        key = key

c_ LFUCache(o..):

    ___ - , capacity):
        """
        :type capacity: int
        """
        capacity = capacity
        hashmap    # dict
        freqMap    # dict
        length = 0
        head = Node(-1, -1)
        tail = Node(-1, -1)
        head.next = tail
        head.freq = f__('-inf')
        tail.freq = f__('inf')
    
    ___ get  key):
        """
        :type key: int
        :rtype: int
        """
        __ key n.. __ hashmap:
            r.. -1
        ____:
            value = hashmap[key].val
            updateNode(hashmap[key])
            r.. value
    
    ___ put  key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        __ capacity __ 0:
            r..
        __ key __ hashmap:
            hashmap[key].val = value
            updateNode(hashmap[key])
        ____:
            __ capacity > length:
                length += 1
                node = Node(key, value)
                hashmap[key] = node
                node.freq = 1
                __ 1 __ freqMap:
                    tmp = freqMap[1][1] # tail of freq
                    nextNode = tmp.next
                    tmp.next = node
                    node.prev = tmp
                    node.next = nextNode
                    node.next.prev = node
                    freqMap[1][1] = node
                ____:
                    nextNode = head.next
                    node.next = nextNode
                    node.prev = head
                    nextNode.prev = node
                    head.next = node
                    freqMap[1] = [node, node]
            ____:
                node = Node(key, value)
                hashmap[key] = node
                firstNode = head.next
                freq = firstNode.freq
                __ freqMap[freq][0] __ freqMap[freq][1]:
                    head.next = firstNode.next
                    firstNode.next.prev = head
                    del freqMap[freq]
                ____:
                    freqMap[freq][0] = freqMap[freq][0].next
                    head.next = firstNode.next
                    firstNode.next.prev = head
                del hashmap[firstNode.key]
                __ 1 __ freqMap:
                    tmp = freqMap[1][1] # tail of freq
                    nextNode = tmp.next
                    tmp.next = node
                    node.prev = tmp
                    node.next = nextNode
                    node.next.prev = node
                    freqMap[1][1] = node
                ____:
                    nextNode = head.next
                    nextNode.prev = node
                    node.next = nextNode
                    head.next = node
                    node.prev = head
                    freqMap[1] = [node, node]
    
    ___ updateNode  node):
        freq = node.freq
        nextNode = freqMap[freq][1].next
        node.prev.next = node.next
        node.next.prev = node.prev
        __ freqMap[freq][0] __ freqMap[freq][1]:
            del freqMap[freq]
        ____:
            __ freqMap[freq][0] __ node:
                freqMap[freq][0] = node.next
            __ freqMap[freq][1] __ node:
                freqMap[freq][1] = node.prev
        node.freq += 1
        freq += 1
        __ freq __ freqMap:
            tail = freqMap[freq][1]
            node.next = tail.next
            tail.next = node
            node.next.prev = node
            node.prev = tail
            freqMap[freq][1] = node
        ____:
            prevNode = nextNode.prev
            prevNode.next = node
            node.next = nextNode
            nextNode.prev = node
            node.prev = prevNode
            freqMap[freq] = [node, node]
