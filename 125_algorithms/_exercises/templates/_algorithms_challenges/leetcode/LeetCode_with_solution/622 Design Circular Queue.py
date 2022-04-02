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

MyCircularQueue(k): Constructor, set the size of the queue to be k.
Front: Get the front item from the queue. If the queue is empty, return -1.
Rear: Get the last item from the queue. If the queue is empty, return -1.
enQueue(value): Insert an element into the circular queue. Return true if the
operation is successful.
deQueue(): Delete an element from the circular queue. Return true if the
operation is successful.
isEmpty(): Checks whether the circular queue is empty or not.
isFull(): Checks whether the circular queue is full or not.
"""


c_ MyCircularQueue:

    ___ - , k: i..
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        head = 0
        tail = -1
        sz = 0
        k = k
        lst = [N.. ___ _ __ r..(k)]


    ___ enQueue  value: i..) __ b..:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        __ sz >= k:
            r.. F..

        tail += 1
        lst[tail % k] = value
        sz += 1
        r.. T..

    ___ deQueue(self) __ b..:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        __ sz <= 0:
            r.. F..

        lst[head % k] = N..
        head += 1
        sz -= 1
        r.. T..

    ___ Front(self) __ i..:
        """
        Get the front item from the queue.
        """
        ret = lst[head % k]
        r.. ret __ ret __ n.. N.. ____ -1

    ___ Rear(self) __ i..:
        """
        Get the last item from the queue.
        """
        ret = lst[tail % k]
        r.. ret __ ret __ n.. N.. ____ -1

    ___ isEmpty(self) __ b..:
        """
        Checks whether the circular queue is empty or not.
        """
        r.. sz __ 0

    ___ isFull(self) __ b..:
        """
        Checks whether the circular queue is full or not.
        """
        r.. sz __ k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
