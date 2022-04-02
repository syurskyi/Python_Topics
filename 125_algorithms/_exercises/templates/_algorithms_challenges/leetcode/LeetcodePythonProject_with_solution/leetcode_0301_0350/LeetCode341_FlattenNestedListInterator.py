'''
Created on Mar 20, 2017

@author: MT
'''

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
c_ NestedInteger(o..
    ___ isInteger
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """
        p..

    ___ getInteger
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """
        p..

    ___ getList
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """
        p..

c_ NestedIterator(o..
    ___ - , nestedList
        d.. = nestedList
        result    # list
        w.... d..:
            ni = d...pop(0)
            __ ni.isInteger
                result.a..(ni.getInteger
            ____:
                l = ni.getList()
                l.r..
                ___ ni0 __ l:
                    d...insert(0, ni0)
        result = result

    ___ next
        r.. result.pop(0)

    ___ hasNext
        __ result:
            r.. T..
        r.. F..

