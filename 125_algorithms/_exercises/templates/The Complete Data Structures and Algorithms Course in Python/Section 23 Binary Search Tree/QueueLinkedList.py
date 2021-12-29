#   Created by Elshad Karimov on 30/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.


c_ Node:
    ___  -   valueN..
        value  value
        next  N..
    
    ___ __str__(self
        r_ st.(value)

c_ LinkedList:
    ___  - (self
        head  N..
        tail  N..
    
    

c_ Queue:
    ___  - (self
        linkedList  LinkedList()
    
    ___ __str__(self
        values  [st.(x) ___ x __ linkedList]
        r_ ' '.j..(values)
    
    ___ enqueue  value
        newNode  Node(value)
        __ linkedList.head __ N..:
            linkedList.head  newNode
            linkedList.tail  newNode
        ____
            linkedList.tail.next  newNode
            linkedList.tail  newNode
    
    ___ isEmpty(self
        __ linkedList.head __ N..:
            r_ T..
        ____
            r_ F..
    
    ___ dequeue(self
        __ isEmpty(
            r_ "There is not any node in the Queue"
        ____
            tempNode  linkedList.head
            __ linkedList.head __ linkedList.tail:
                linkedList.head  N..
                linkedList.tail  N..
            ____
                linkedList.head  linkedList.head.next
            r_ tempNode
    
    ___ peek(self
        __ isEmpty(
            r_ "There is not any node in the Queue"
        ____
            r_ linkedList.head
    
    ___ delete(self
        linkedList.head  N..
        linkedList.tail  N..




# custQueue = Queue()
# custQueue.enqueue(1)
# custQueue.enqueue(2)
# custQueue.enqueue(3)
# print(custQueue)
# print(custQueue.peek())
# print(custQueue)