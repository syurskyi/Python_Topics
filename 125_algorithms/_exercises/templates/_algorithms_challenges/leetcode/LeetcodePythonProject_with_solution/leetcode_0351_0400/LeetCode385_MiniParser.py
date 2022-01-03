'''
Created on Apr 2, 2017

@author: MT
'''

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
c_ NestedInteger(object):
    ___ - , value_ N..
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """
        pass

    ___ isInteger
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """
        pass

    ___ add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """
        pass

    ___ setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
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

c_ Solution(object):
    ___ deserialize(self, s):
        __ s[0] __ '[' a.. s[-1] __ ']':
            nestedInt = NestedInteger()
            s = s[1:-1]
            __ n.. s: r.. nestedInt
            i, prev= 0, 0
            w.... i < l..(s):
                __ s[i] __ '[':
                    count = 1
                    w.... i < l..(s) a.. count > 0:
                        i+=1
                        __ s[i] __ ']':
                            count -= 1
                        ____ s[i] __ '[':
                            count += 1
                    nestedInt.add(deserialize(s[prev:i+1]))
                    i+=1
                    prev = i+1
                ____ s[i] __ ',':
                    nestedInt.add(int(s[prev:i]))
                    prev = i+1
                i+=1
            r.. nestedInt
        ____:
            nestedInt = NestedInteger()
            __ s:
                nestedInt.setInteger(int(s))
            r.. nestedInt

