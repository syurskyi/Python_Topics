#   Created by Elshad Karimov on 29/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

class Queue:
    ___ __init__(self, maxSize
        self.items = maxSize * [None]
        self.maxSize = maxSize
        self.start = -1
        self.top = -1 
    
    ___ __str__(self
        values = [str(x) for x in self.items]
        return ' '.join(values)
    
    ___ isFull(self
        __ self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.maxSize:
            return True
        ____
            return False
    
    ___ isEmpty(self
        __ self.top == -1:
            return True
        ____
            return False
    
    ___ enqueue(self, value
        __ self.isFull(
            return "The queue is full"
        ____
            __ self.top + 1 == self.maxSize:
                self.top = 0
            ____
                self.top += 1
                __ self.start == -1:
                    self.start = 0
            self.items[self.top] = value
            return "The element is inserted at the end of Queue"
    
    ___ dequeue(self
        __ self.isEmpty(
            return "There is not any element in the Queue"
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
            return firstElement
    
    ___ peek(self
        __ self.isEmpty(
            return "There is not any element in the Queue"
        ____
            return self.items[self.start]
    
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