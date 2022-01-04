"""
Given a nested list of integers represented as a string, implement a parser to deserialize it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Note: You may assume that the string is well-formed:

String is non-empty.
String does not contain white spaces.
String contains only digits 0-9, [, - ,, ].
Example 1:

Given s = "324",

You should return a NestedInteger object which contains a single integer 324.
Example 2:

Given s = "[123,[456,[789]]]",

Return a NestedInteger object containing a nested list with 2 elements:

1. An integer containing value 123.
2. A nested list containing two elements:
    i.  An integer containing value 456.
    ii. A nested list with one element:
         a. An integer containing value 789.
"""
__author__ = 'Daniel'

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
    ___ isInteger
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """

    ___ add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """

    ___ setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """

    ___ getInteger
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """

    ___ getList
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """


c_ Solution(object):
    ___ deserialize(self, s):
        """
        NestedInteger is a UnionType in functional programming jargon.

        [1, [1, [2]], 3, 4]
        From a general example, develop an algorithm using stack
        The algorithm itself is easy, but the string parsing contains lots of edge cases
        :type s: str
        :rtype: NestedInteger
        """
        __ n.. s: r.. N..
        stk    # list

        i = 0
        w.... i < l..(s):
            __ s[i] __ '[':
                stk.a..(NestedInteger())
                i += 1
            ____ s[i] __ ']':
                ni = stk.pop()
                __ n.. stk: r.. ni

                stk[-1].add(ni)
                i += 1
            ____ s[i] __ ',':
                i += 1
            ____:
                j = i
                w.... j < l..(s) a.. (s[j].isdigit() o. s[j] __ '-'): j += 1

                ni = NestedInteger(i..(s[i: j]) __ s[i: j] ____ N..)
                __ n.. stk: r.. ni
                stk[-1].add(ni)
                i = j

        r.. stk.pop()


__ __name__ __ "__main__":
    Solution().deserialize("[123,[456,[789]]]")








