'''
Created on Feb 9, 2017

@author: MT
'''

c_ Node(o..
    ___ - , key, val, prevNode=N.., nextNode_ N..
        key = key
        val = val
        prev = prevNode
        next = nextNode

c_ LRUCache(o..
    ___ - , capacity
        """
        :type capacity: int
        """
        map    # dict
        capacity = capacity
        head = N..
        tail = N..
    
    ___ removeAndAppend  key
        node = map[key]
        prevNode = node.prev
        nextNode = node.next
        __ prevNode:
            prevNode.next = node.next
            __ nextNode:
                nextNode.prev = prevNode
                tail.next = node
                node.prev = tail
            ____
                prevNode.next = node
                node.prev = prevNode
        ____
            __ next:
                head = nextNode
                nextNode.prev = N..
                tail.next = node
                node.prev = tail
            ____
                head = node
        tail = node
        head.prev = N..
        tail.next = N..
    
    ___ get  key
        __ key n.. __ map:
            r.. -1
        ____
            node = map[key]
            val = node.val
            removeAndAppend(key)
            r.. val
    
    ___ s..  key, value
        __ n.. map:
            node = Node(key, value)
            map[key] = node
            head = node
            tail = node
        ____
            __ key __ map:
                removeAndAppend(key)
                tail.val = value
            ____
                __ l.. m..) < capacity:
                    node = Node(key, value)
                    tail.next = node
                    node.prev = tail
                    tail = node
                    map[key] = node
                ____ l.. m..) __ capacity:
                    node = Node(key, value)
                    map[key] = node
                    tmpHead = head
                    del map[tmpHead.key]
                    __ head.next:
                        head = head.next
                        head.prev = N..
                        tail.next = node
                        node.prev = tail
                        tail = node
                    ____
                        head = node
                        tail = node

__ _____ __ _____
    cache = LRUCache(2)
    cache.s..(1, 1)
    cache.s..(2, 2)
    print(cache.g.. 1
    cache.s..(3, 3)
    print(cache.g.. 2
    cache.s..(4, 4)
    print(cache.g.. 1
    print(cache.g.. 3
    print(cache.g.. 4
