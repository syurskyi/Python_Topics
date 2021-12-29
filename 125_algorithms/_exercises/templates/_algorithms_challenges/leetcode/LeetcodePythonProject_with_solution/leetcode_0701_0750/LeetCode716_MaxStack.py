'''
Created on Feb 14, 2018

@author: tongq
'''
_______ heapq

class MaxStack(object):

    ___ __init__(self):
        """
        initialize your data structure here.
        """
        self.stack    # list
        self.heap    # list

    ___ push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.a..(x)
        heapq.heappush(self.heap, (-x))

    ___ pop(self):
        """
        :rtype: int
        """
        val = self.stack.pop()
        self.heap.remove((-val))
        heapq.heapify(self.heap)
        r.. val

    ___ top(self):
        """
        :rtype: int
        """
        r.. self.stack[-1]

    ___ peekMax(self):
        """
        :rtype: int
        """
        r.. -self.heap[0]

    ___ popMax(self):
        """
        :rtype: int
        """
        val = heapq.heappop(self.heap)
        val = -val
        ___ i __ r..(l..(self.stack)-1, -1, -1):
            __ self.stack[i] __ val:
                self.stack = self.stack[:i]+self.stack[i+1:]
                break
        r.. val
