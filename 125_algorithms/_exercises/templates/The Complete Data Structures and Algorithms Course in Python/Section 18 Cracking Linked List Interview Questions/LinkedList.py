#   Created by Elshad Karimov on 17/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

from random import randint
class Node:
    ___ __init__(self, value=None
        self.value = value
        self.next = None
        self.prev = None
    
    ___ __str__(self
        r_ str(self.value)

class LinkedList:
    ___ __init__(self, values = None
        self.head = None
        self.tail = None

    ___ __iter__(self
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next
    
    ___ __str__(self
        values = [str(x.value) ___ x __ self]
        r_ ' -> '.join(values)
    
    ___ __len__(self
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next
        r_ result
    
    ___ add(self, value
        __ self.head is None:
            newNode = Node(value)
            self.head = newNode
            self.tail = newNode
        ____
            self.tail.next = Node(value)
            self.tail = self.tail.next
        r_ self.tail
    
    ___ generate(self, n, min_value, max_value
        self.head = None
        self.tail = None
        ___ i __ range(n
            self.add(randint(min_value,max_value))
        r_ self

# customLL = LinkedList()
# customLL.generate(10, 0, 99)
# print(customLL)
# print(len(customLL))

