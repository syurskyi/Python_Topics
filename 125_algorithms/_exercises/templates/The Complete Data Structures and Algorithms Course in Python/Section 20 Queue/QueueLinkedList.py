#   Created by Elshad Karimov on 30/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.


c_ Node:
    ___  -   value=N..
        value = value
        next = N..
    
    ___ __str__(self
        r_ str(value)

c_ LinkedList:
    ___  - (self
        head = N..
        tail = N..
    
    ___ __iter__(self
        curNode = head
        while curNode:
            yield curNode
            curNode = curNode.next

c_ Queue:
    ___  - (self
        linkedList = LinkedList()
    
    ___ __str__(self
        values = [str(x) ___ x __ linkedList]
        r_ ' '.join(values)
    
    ___ enqueue  value
        newNode = Node(value)
        __ linkedList.head __ N..:
            linkedList.head = newNode
            linkedList.tail = newNode
        ____
            linkedList.tail.next = newNode
            linkedList.tail = newNode
    
    ___ isEmpty(self
        __ linkedList.head __ N..:
            r_ T..
        ____
            r_ F..
    
    ___ dequeue(self
        __ isEmpty(
            r_ "There is not any node in the Queue"
        ____
            tempNode = linkedList.head
            __ linkedList.head __ linkedList.tail:
                linkedList.head = N..
                linkedList.tail = N..
            ____
                linkedList.head = linkedList.head.next
            r_ tempNode
    
    ___ peek(self
        __ isEmpty(
            r_ "There is not any node in the Queue"
        ____
            r_ linkedList.head
    
    ___ delete(self
        linkedList.head = N..
        linkedList.tail = N..




custQueue = Queue()
custQueue.enqueue(1)
custQueue.enqueue(2)
custQueue.enqueue(3)
print(custQueue)
print(custQueue.peek())
print(custQueue)