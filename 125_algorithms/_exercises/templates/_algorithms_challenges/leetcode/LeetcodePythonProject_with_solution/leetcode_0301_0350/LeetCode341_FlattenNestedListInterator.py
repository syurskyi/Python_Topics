'''
Created on Mar 20, 2017

@author: MT
'''

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
c_ NestedInteger(object):
    ___ isInteger
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """
        pass

    ___ getInteger
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """
        pass

    ___ getList
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """
        pass

c_ NestedIterator(object):
    ___ - , nestedList):
        deque = nestedList
        result    # list
        w.... deque:
            ni = deque.pop(0)
            __ ni.isInteger():
                result.a..(ni.getInteger())
            ____:
                l = ni.getList()
                l.reverse()
                ___ ni0 __ l:
                    deque.insert(0, ni0)
        result = result

    ___ next
        r.. result.pop(0)

    ___ hasNext
        __ result:
            r.. T..
        r.. F..

