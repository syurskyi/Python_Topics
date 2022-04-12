'''
Created on Feb 14, 2018

@author: tongq
'''
_______ h__

c_ MaxStack(o..

    ___ -
        """
        initialize your data structure here.
        """
        stack    # list
        heap    # list

    ___ push  x
        """
        :type x: int
        :rtype: void
        """
        stack.a..(x)
        h__.heappush(heap, (-x

    ___ pop
        """
        :rtype: int
        """
        val stack.p.. )
        heap.remove((-val
        h__.heapify(heap)
        r.. val

    ___ top
        """
        :rtype: int
        """
        r.. stack[-1]

    ___ peekMax
        """
        :rtype: int
        """
        r.. -heap[0]

    ___ popMax
        """
        :rtype: int
        """
        val h__.heappop(heap)
        val -val
        ___ i __ r..(l..(stack)-1, -1, -1
            __ stack[i] __ val:
                stack stack[:i]+stack[i+1:]
                _____
        r.. val
