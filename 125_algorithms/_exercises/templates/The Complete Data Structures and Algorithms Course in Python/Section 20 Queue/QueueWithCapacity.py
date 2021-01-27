#   Created by Elshad Karimov on 29/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

class Queue:
    ___ __init__(self, maxSize
        self.items = maxSize * [None]
        self.maxSize = maxSize
        self.start = -1
        self.top = -1 
    
    ___ __str__(self
        values = [str(x) ___ x __ self.items]
        r_ ' '.join(values)
    
    ___ isFull(self
        __ self.top + 1 == self.start:
            r_ True
        elif self.start == 0 and self.top + 1 == self.maxSize:
            r_ True
        ____
            r_ False
    
    ___ isEmpty(self
        __ self.top == -1:
            r_ True
        ____
            r_ False
    
    ___ enqueue(self, value
        __ self.isFull(
            r_ "The queue is full"
        ____
            __ self.top + 1 == self.maxSize:
                self.top = 0
            ____
                self.top += 1
                __ self.start == -1:
                    self.start = 0
            self.items[self.top] = value
            r_ "The element is inserted at the end of Queue"
    
    ___ dequeue(self
        __ self.isEmpty(
            r_ "There is not any element in the Queue"
        ____
            firstElement = self.items[self.start]
            start = self.start
            __ self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start + 1 == self.maxSize:
                self.start = 0
            ____
                self.start += 1
            self.items[start] = None
            r_ firstElement
    
    ___ peek(self
        __ self.isEmpty(
            r_ "There is not any element in the Queue"
        ____
            r_ self.items[self.start]
    
    ___ delete(self
        self.items = self.maxSize * [None]
        self.top = -1
        self.start = -1






customQueue = Queue(3)
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
customQueue.delete()
print(customQueue)