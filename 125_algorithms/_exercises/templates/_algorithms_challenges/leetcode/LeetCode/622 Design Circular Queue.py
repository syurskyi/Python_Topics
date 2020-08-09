#!/usr/bin/python3
"""
Design your implementation of the circular queue. The circular queue is a
linear data structure in which the operations are performed based on FIFO (First
In First Out) principle and the last position is connected back to the first
position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces
in front of the queue. In a normal queue, once the queue becomes full, we cannot
insert the next element even if there is a space in front of the queue. But
using the circular queue, we can use the space to store new values.

Your implementation should support following operations:

MyCircularQueue(k Constructor, set the size of the queue to be k.
Front: Get the front item from the queue. If the queue is empty, return -1.
Rear: Get the last item from the queue. If the queue is empty, return -1.
enQueue(value Insert an element into the circular queue. Return true if the
operation is successful.
deQueue( Delete an element from the circular queue. Return true if the
operation is successful.
isEmpty( Checks whether the circular queue is empty or not.
isFull( Checks whether the circular queue is full or not.
"""


class MyCircularQueue:

    ___ __init__(self, k: int
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.head = 0
        self.tail = -1
        self.sz = 0
        self.k = k
        self.lst = [None for _ in range(k)]


    ___ enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        __ self.sz >= self.k:
            r_ False

        self.tail += 1
        self.lst[self.tail % self.k] = value
        self.sz += 1
        r_ True

    ___ deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        __ self.sz <= 0:
            r_ False

        self.lst[self.head % self.k] = None
        self.head += 1
        self.sz -= 1
        r_ True

    ___ Front(self) -> int:
        """
        Get the front item from the queue.
        """
        ret = self.lst[self.head % self.k]
        r_ ret __ ret is not None else -1

    ___ Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        ret = self.lst[self.tail % self.k]
        r_ ret __ ret is not None else -1

    ___ isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        r_ self.sz __ 0

    ___ isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        r_ self.sz __ self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
