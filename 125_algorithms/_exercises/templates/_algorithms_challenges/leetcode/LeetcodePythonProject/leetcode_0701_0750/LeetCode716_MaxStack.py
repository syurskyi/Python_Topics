'''
Created on Feb 14, 2018

@author: tongq
'''
______ heapq

class MaxStack(object

    ___ __init__(self
        """
        initialize your data structure here.
        """
        self.stack = []
        self.heap = []

    ___ push(self, x
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        heapq.heappush(self.heap, (-x))

    ___ pop(self
        """
        :rtype: int
        """
        val = self.stack.p..
        self.heap.remove((-val))
        heapq.heapify(self.heap)
        r_ val

    ___ top(self
        """
        :rtype: int
        """
        r_ self.stack[-1]

    ___ peekMax(self
        """
        :rtype: int
        """
        r_ -self.heap[0]

    ___ popMax(self
        """
        :rtype: int
        """
        val = heapq.heappop(self.heap)
        val = -val
        ___ i in range(le.(self.stack)-1, -1, -1
            __ self.stack[i] __ val:
                self.stack = self.stack[:i]+self.stack[i+1:]
                break
        r_ val
