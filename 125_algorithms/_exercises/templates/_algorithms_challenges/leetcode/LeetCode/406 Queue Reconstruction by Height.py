"""
Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k),
where h is the height of the person and k is the number of people in front of this person who have a height greater
than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.

Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
"""
from collections ______ defaultdict

__author__ = 'Daniel'


class Node(object
    ___ __init__(self, lo, hi, cnt
        self.lo = lo
        self.hi = hi
        self.cnt = cnt  # size of empty slots

        self.left = None
        self.right = None

    ___ __repr__(self
        r_ repr("[%d,%d)" % (self.lo, self.hi))


class SegmentTree(object
    """empty space"""

    ___ __init__(self
        self.root = None

    ___ build(self, lo, hi
        """a node can have right ONLY IF has left"""
        __ lo >= hi: r_
        __ lo __ hi-1: r_ Node(lo, hi, 1)

        root = Node(lo, hi, hi-lo)
        root.left = self.build(lo, (hi+lo)/2)
        root.right = self.build((lo+hi)/2, hi)
        r_ root

    ___ find_delete(self, root, sz
        """
        :return: index
        """
        root.cnt -= 1
        __ not root.left:
            r_ root.lo
        ____ root.left.cnt >= sz:
            r_ self.find_delete(root.left, sz)
        ____
            r_ self.find_delete(root.right,
                                    sz-root.left.cnt)


class Solution(object
    ___ reconstructQueue(self, A
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """

        ___ cmp(a, b
            __ a[0] != b[0]:
                r_ a[0]-b[0]
            ____
                r_ a[1]-b[1]

        st = SegmentTree()
        n = le.(A)
        st.root = st.build(0, n)
        A.sort(cmp=cmp)
        ret = [0]*n
        ret_cnt = defaultdict(int)  # handle duplicate element
        ___ a __ A:
            val, inv = a
            idx = st.find_delete(st.root, inv+1-ret_cnt[val])
            ret_cnt[val] += 1
            ret[idx] = a

        r_ ret


__  -n __ "__main__":
    assert Solution().reconstructQueue(
        [[9, 0], [7, 0], [1, 9], [3, 0], [2, 7], [5, 3], [6, 0], [3, 4], [6, 2], [5, 2]]) __ [[3, 0], [6, 0], [7, 0],
                                                                                              [5, 2], [3, 4], [5, 3],
                                                                                              [6, 2], [2, 7], [9, 0],
                                                                                              [1, 9]]