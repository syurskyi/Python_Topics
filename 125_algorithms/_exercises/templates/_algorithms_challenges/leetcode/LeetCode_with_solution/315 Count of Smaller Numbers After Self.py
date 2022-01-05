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


c_ TreeNode(object):
    ___ - , start, end, cnt=0):
        start = start
        end = end
        cnt = cnt
        left = N..
        right = N..


c_ SegmentTree(object):
    ___ - , n):
        root = build(0, n)

    ___ build  start, end):
        __ start >= end: r..
        __ start __ end-1: r.. TreeNode(start, end)
        node = TreeNode(start, end)
        node.left = build(start, (start+end)/2)
        node.right = build((start+end)/2, end)
        r.. node

    ___ inc  idx, val):
        cur = root
        w.... cur:
            cur.cnt += val
            mid = (cur.start+cur.end)/2
            __ cur.start <= idx < mid:
                cur = cur.left
            ____ mid <= idx < cur.end:
                cur = cur.right
            ____:
                r..

    ___ query_less  cur, idx):
        __ n.. cur:
            r.. 0

        mid = (cur.start+cur.end)/2
        __ cur.start <= idx < mid:
            r.. query_less(cur.left, idx)
        ____ mid <= idx < cur.end:
            r.. (cur.left.cnt __ cur.left ____ 0) + query_less(cur.right, idx)
        ____:
            r.. 0


c_ Solution(object):
    ___ countSmaller  nums):
        """
        Brute force: O(n^2)
        Segment Tree
        O(n lg n)
        :type nums: List[int]
        :rtype: List[int]
        """
        # preprocess the array to make it discrete in [0, 1, ..., n-1]
        h    # dict
        ___ i, v __ e..(s..(nums)):
            h[v] = i  # override duplicates

        A = [h[v] ___ v __ nums]
        n = l..(A)
        st = SegmentTree(n)
        ret    # list
        ___ i __ xrange(n-1, -1, -1):
            ret.a..(st.query_less(st.root, A[i]))
            st.inc(A[i], 1)

        r.. ret[::-1]


__ _______ __ _______
    ... Solution().countSmaller([5, 2, 6, 1]) __ [2, 1, 1, 0]
    ... Solution().countSmaller([-1, -1]) __ [0, 0]
