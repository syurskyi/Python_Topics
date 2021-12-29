"""
You are given an integer array nums and you have to return a new counts array. The counts array has the property where
counts[i] is the number of smaller elements to the right of nums[i].

Example:

Given nums = [5, 2, 6, 1]

To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
Return the array [2, 1, 1, 0].
"""
__author__ = 'Daniel'


class TreeNode(object):
    ___ __init__(self, start, end, cnt=0):
        self.start = start
        self.end = end
        self.cnt = cnt
        self.left = N..
        self.right = N..


class SegmentTree(object):
    ___ __init__(self, n):
        self.root = self.build(0, n)

    ___ build(self, start, end):
        __ start >= end: r..
        __ start __ end-1: r.. TreeNode(start, end)
        node = TreeNode(start, end)
        node.left = self.build(start, (start+end)/2)
        node.right = self.build((start+end)/2, end)
        r.. node

    ___ inc(self, idx, val):
        cur = self.root
        while cur:
            cur.cnt += val
            mid = (cur.start+cur.end)/2
            __ cur.start <= idx < mid:
                cur = cur.left
            ____ mid <= idx < cur.end:
                cur = cur.right
            ____:
                r..

    ___ query_less(self, cur, idx):
        __ n.. cur:
            r.. 0

        mid = (cur.start+cur.end)/2
        __ cur.start <= idx < mid:
            r.. self.query_less(cur.left, idx)
        ____ mid <= idx < cur.end:
            r.. (cur.left.cnt __ cur.left ____ 0) + self.query_less(cur.right, idx)
        ____:
            r.. 0


class Solution(object):
    ___ countSmaller(self, nums):
        """
        Brute force: O(n^2)
        Segment Tree
        O(n lg n)
        :type nums: List[int]
        :rtype: List[int]
        """
        # preprocess the array to make it discrete in [0, 1, ..., n-1]
        h = {}
        ___ i, v __ enumerate(s..(nums)):
            h[v] = i  # override duplicates

        A = [h[v] ___ v __ nums]
        n = l..(A)
        st = SegmentTree(n)
        ret    # list
        ___ i __ xrange(n-1, -1, -1):
            ret.a..(st.query_less(st.root, A[i]))
            st.inc(A[i], 1)

        r.. ret[::-1]


__ __name__ __ "__main__":
    ... Solution().countSmaller([5, 2, 6, 1]) __ [2, 1, 1, 0]
    ... Solution().countSmaller([-1, -1]) __ [0, 0]
