"""
Your NestedIterator object will be instantiated and called as such:
i, v = NestedIterator(nestedList), []
while i.hasNext(): v.append(i.next())


This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation

class NestedInteger(object):
    def isInteger(self):
        # @return {boolean} True if this NestedInteger holds a single integer,
        # rather than a nested list.

    def getInteger(self):
        # @return {int} the single integer that this NestedInteger holds,
        # if it holds a single integer
        # Return None if this NestedInteger holds a nested list

    def getList(self):
        # @return {NestedInteger[]} the nested list that this NestedInteger holds,
        # if it holds a nested list
        # Return None if this NestedInteger holds a single integer
"""


c_ NestedIterator(o..
    ___ - , nestedList
        stack [[nestedList, 0]]

    # @return {int} the next element in the iteration
    ___ next
        __ n.. hasNext
            r.. -1

        lst, i stack[-1]
        stack[-1][1] += 1

        r.. lst[i].getInteger()

    # @return {boolean} true if the iteration has more element or false
    ___ hasNext
        stack stack

        w.... stack:
            lst, i stack[-1]

            __ i >_ l..(lst
                stack.p.. )
            ____ lst[i].isInteger
                r.. T..
            ____
                # lst[i] is list
                stack[-1][1] += 1
                stack.a..([lst[i].getList(), 0])

        r.. F..
