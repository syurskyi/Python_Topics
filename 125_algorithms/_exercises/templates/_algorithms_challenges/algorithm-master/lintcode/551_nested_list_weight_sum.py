"""
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


c_ Solution(o..
    # @param {NestedInteger[]} L a list of NestedInteger Object
    # @return {int} an integer
    ___ depthSum  L
        r.. dfs(L, 1)

    ___ dfs  L, depth
        _sum = 0

        ___ obj __ L:
            __ obj.isInteger
                _sum += depth * obj.getInteger()
                _____

            _sum += dfs(obj.getList(), depth + 1)

        r.. _sum


c_ Solution(o..
    # @param {NestedInteger[]} L a list of NestedInteger Object
    # @return {int} an integer
    ___ depthSum  L
        ans = 0
        __ n.. L:
            r.. ans

        queue = L
        depth = 0
        w.... queue:
            _queue    # list
            depth += 1

            ___ obj __ queue:
                __ obj.isInteger
                    ans += depth * obj.getInteger()
                    _____

                _queue.extend(obj.getList())

            queue = _queue

        r.. ans
