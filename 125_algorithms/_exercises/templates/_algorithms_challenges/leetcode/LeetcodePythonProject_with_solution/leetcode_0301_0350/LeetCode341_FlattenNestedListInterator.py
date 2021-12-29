'''
Created on Mar 20, 2017

@author: MT
'''

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger(object):
    ___ isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """
        pass

    ___ getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """
        pass

    ___ getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """
        pass

class NestedIterator(object):
    ___ __init__(self, nestedList):
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
        self.result = result

    ___ next(self):
        r.. self.result.pop(0)

    ___ hasNext(self):
        __ self.result:
            r.. True
        r.. False

