#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com
# @Last Modified time: 2016-07-09 14:22:29

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """


c.. NestedIterator o..
    """
    According to:
    https://discuss.leetcode.com/topic/42042/simple-java-solution-using-a-stack-with-explanation

    In the constructor, we push all the nestedList into the stack from back to front,
    so when we pop the stack, it returns the very first element.
    Second, in the hasNext() function, we peek the first element in stack currently,
    and if it is an Integer, we will return true and pop the element.

    If it is a list, we will further flatten it.
    This is iterative version of flatting the nested list.
    Again, we need to iterate from the back to front of the list.
    """
    ___ __init__  nestedList
        """Initialize your data structure here.

        :type nestedList: List[NestedInteger]
        """
        self.stack   # list
        ___ item __ nestedList[::-1]:
            self.stack.append(item)

    ___ next(self
        val = self.stack[-1].getInteger()
        self.stack.pop()
        r_ val

    ___ hasNext(self
        _____ self.stack:
            curr = self.stack[-1]
            __ curr.isInteger(
                r_ True
            self.stack.pop()
            __ curr.getList(
                ___ i __ curr.getList()[::-1]:
                    self.stack.append(i)
        r_ False


c.. NestedIterator_2 o..
    """ Python Generators solution

    According to:
    https://discuss.leetcode.com/topic/45844/python-generators-solution
    """
    ___ __init__  nestedList
        """Initialize your data structure here.
        """
        ___ gen(nestedList
            ___ item __ nestedList:
                __ item.isInteger(
                    yield item.getInteger()
                ____
                    ___ list __ gen(item.getList()):
                        yield list

        self.gen = gen(nestedList)

    ___ next(self
        r_ self.value

    ___ hasNext(self
        try:
            self.value = next(self.gen)
            r_ True
        except StopIteration:
            r_ False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

'''
[]
[1,[2,[3]]]
[[1,2],3,[4,5]]
[[[1,2,3], [4,5], 7], [8,9], 10]
'''
