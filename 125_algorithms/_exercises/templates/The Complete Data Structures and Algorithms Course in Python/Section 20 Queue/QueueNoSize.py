#   Created by Elshad Karimov on 29/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

c_ Queue:
    ___  - (self
        items = []
    
    ___ __str__(self
        values = [st.(x) ___ x __ items]
        r_ ' '.j..(values)
    
    ___ isEmpty(self
        __ items __ []:
            r_ T..
        ____
            r_ F..
    
    ___ enqueue  value
        items.ap..(value)
        r_ "The element is inserted at the end of Queue"
    
    ___ dequeue(self
        __ isEmpty(
            r_ "The is not any element in the Queue"
        ____
            r_ items.pop(0)
    
    ___ peek(self
        __ isEmpty(
            r_ "The is not any element in the Queue"
        ____
            r_ items[0]
    
    ___ delete(self
        items = N..




customQueue = Queue()
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue.peek())
customQueue.delete()
