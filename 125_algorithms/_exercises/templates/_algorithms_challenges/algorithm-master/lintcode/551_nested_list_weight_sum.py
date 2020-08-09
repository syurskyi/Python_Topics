"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation

class NestedInteger(object
    ___ isInteger(self
        # @return {boolean} True if this NestedInteger holds a single integer,
        # rather than a nested list.

    ___ getInteger(self
        # @return {int} the single integer that this NestedInteger holds,
        # if it holds a single integer
        # Return None if this NestedInteger holds a nested list

    ___ getList(self
        # @return {NestedInteger[]} the nested list that this NestedInteger holds,
        # if it holds a nested list
        # Return None if this NestedInteger holds a single integer
"""


class Solution(object
    # @param {NestedInteger[]} L a list of NestedInteger Object
    # @return {int} an integer
    ___ depthSum(self, L
        r_ self.dfs(L, 1)

    ___ dfs(self, L, depth
        _sum = 0

        ___ obj in L:
            __ obj.isInteger(
                _sum += depth * obj.getInteger()
                continue

            _sum += self.dfs(obj.getList(), depth + 1)

        r_ _sum


class Solution(object
    # @param {NestedInteger[]} L a list of NestedInteger Object
    # @return {int} an integer
    ___ depthSum(self, L
        ans = 0
        __ not L:
            r_ ans

        queue = L
        depth = 0
        w___ queue:
            _queue = []
            depth += 1

            ___ obj in queue:
                __ obj.isInteger(
                    ans += depth * obj.getInteger()
                    continue

                _queue.extend(obj.getList())

            queue = _queue

        r_ ans
