#   Created by Elshad Karimov on 29/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

class Queue:
    ___ __init__(self
        self.items = []
    
    ___ __str__(self
        values = [str(x) ___ x __ self.items]
        r_ ' '.join(values)
    
    ___ isEmpty(self
        __ self.items == []:
            r_ True
        ____
            r_ False
    
    ___ enqueue(self, value
        self.items.append(value)
        r_ "The element is inserted at the end of Queue"
    
    ___ dequeue(self
        __ self.isEmpty(
            r_ "The is not any element in the Queue"
        ____
            r_ self.items.pop(0)
    
    ___ peek(self
        __ self.isEmpty(
            r_ "The is not any element in the Queue"
        ____
            r_ self.items[0]
    
    ___ delete(self
        self.items = None




customQueue = Queue()
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue.peek())
customQueue.delete()
