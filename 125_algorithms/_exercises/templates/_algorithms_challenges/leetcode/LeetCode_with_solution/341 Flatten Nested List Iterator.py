"""
Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:
Given the list [[1,1],2,[1,1]],

By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].

Example 2:
Given the list [1,[4,[6]]],

By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].
"""
__author__ 'Daniel'


"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation
"""


c_ NestedInteger(o..
    ___ isInteger
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """
        r.. T..

    ___ getInteger
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """
        r.. 0

    ___ getList
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """
        r.. []


c_ NestedIterator(o..
    ___ - , nestedList
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]

        Linear structure usually use stack as structure.
        Iterator Invariant:
        1. has the value to be returned ready: idx pointing to the integer to be return in the next().
        2. rember move the parent pointer in hasNext()

        Possible to compile nl and idx into a tuple.
        """
        stk [[nestedList, 0]]  # stack of iterators

    ___ next
        """
        :rtype: int
        """
        nl, idx stk[-1]
        nxt nl[idx].getInteger()
        stk[-1][1] idx + 1  # advance the index
        r.. nxt

    ___ hasNext
        """
        Put the pointer movement logic in the hasNext()
        :rtype: bool
        """
        w.... stk:
            nl, idx stk[-1]
            __ idx < l..(nl
                ni nl[idx]
                __ ni.isInteger
                    r.. T..
                ____
                    stk[-1][1] idx + 1  # prepare the parent, otherwise dead loop
                    nxt_nl ni.getList()
                    stk.a..([nxt_nl, 0])
            ____
                stk.p.. )

        r.. F..



c_ NestedIteratorVerbose(o..
    ___ - , nestedList
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]

        Iterator Invariant:
        1. has the value to be returned ready: idx pointing to the integer to be return in the next().
        2. move the pointer in hasNext()

        Possible to compile nl and idx into a tuple.
        """
        nl_stk [nestedList]
        idx_stk [0]

    ___ next
        """
        :rtype: int
        """
        __ hasNext
            nl nl_stk[-1]
            idx idx_stk[-1]
            nxt nl[idx]
            idx_stk[-1] idx + 1
            r.. nxt

        r.. S..()

    ___ hasNext
        """
        Put the pointer movement logic in the hasNext()
        :rtype: bool
        """
        w.... nl_stk:
            nl nl_stk[-1]
            idx idx_stk[-1]
            __ idx < l..(nl
                ni nl[idx]
                __ ni.isInteger
                    r.. T..
                ____
                    idx_stk[-1] idx+1
                    nxt_nl ni.getList()
                    nxt_idx 0
                    nl_stk.a..(nxt_nl)
                    idx_stk.a..(nxt_idx)
            ____
                nl_stk.p.. )
                idx_stk.p.. )

        r.. F..


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
