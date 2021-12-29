#   Created by Elshad Karimov on 29/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

c_ Queue:
    ___  -   maxSize
        items  maxSize * [N..]
        maxSize  maxSize
        start  -1
        top  -1
    
    ___ __str__(self
        values  [st.(x) ___ x __ items]
        r_ ' '.j..(values)
    
    ___ isFull(self
        __ top + 1 __ start:
            r_ T..
        ____ start __ 0 a__ top + 1 __ maxSize:
            r_ T..
        ____
            r_ F..
    
    ___ isEmpty(self
        __ top __ -1:
            r_ T..
        ____
            r_ F..
    
    ___ enqueue  value
        __ isFull(
            r_ "The queue is full"
        ____
            __ top + 1 __ maxSize:
                top  0
            ____
                top + 1
                __ start __ -1:
                    start  0
            items[top]  value
            r_ "The element is inserted at the end of Queue"
    
    ___ dequeue(self
        __ isEmpty(
            r_ "There is not any element in the Queue"
        ____
            firstElement  items[start]
            start  start
            __ start __ top:
                start  -1
                top  -1
            ____ start + 1 __ maxSize:
                start  0
            ____
                start + 1
            items[start]  N..
            r_ firstElement
    
    ___ peek(self
        __ isEmpty(
            r_ "There is not any element in the Queue"
        ____
            r_ items[start]
    
    ___ delete(self
        items  maxSize * [N..]
        top  -1
        start  -1






customQueue  Queue(3)
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
customQueue.delete()
print(customQueue)