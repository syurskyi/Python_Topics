#!/usr/bin/python3
"""
Given two arrays A and B of equal size, the advantage of A with respect to B is
the number of indices i for which A[i] > B[i].

Return any permutation of A that maximizes its advantage with respect to B.

Example 1:

Input: A = [2,7,11,15], B = [1,10,4,11]
Output: [2,11,7,15]
Example 2:

Input: A = [12,24,8,32], B = [13,25,32,11]
Output: [24,32,8,12]


Note:

1 <= A.length = B.length <= 10000
0 <= A[i] <= 10^9
0 <= B[i] <= 10^9
"""
____ typing _______ List
____ collections _______ defaultdict


c_ Solution:
    ___ advantageCount(self, A: List[i..], B: List[i..]) __ List[i..]:
        """
        Gready select the smallest larger number
        Then we need sort A
        Iterate B and do a bisect on A? Hard to remove the chosen element on A
        unless using a balanced BST
        How about we sort B also?
        Like a merge sort, compare both sorted A and sorted B
        But we need to record the position of B's element since sorting break the
        position
        Keep a reverse index mapping is not enough, since duplicate in B
        then keep a list
        """
        idxes = defaultdict(l..)
        ___ i, b __ e..(B):
            idxes[b].a..(i)

        n = l..(A)
        A.s..()
        B.s..()
        ret = [N.. ___ _ __ r..(n)]
        not_used    # list
        j = 0
        ___ a __ A:
            __ a > B[j]:
                i = idxes[B[j]].pop()
                ret[i] = a
                j += 1
            ____:
                not_used.a..(a)

        ___ i __ r..(n):
            __ ret[i] __ N..
                ret[i] = not_used.pop()

        r.. ret


__ __name__ __ "__main__":
    ... Solution().advantageCount([2,7,11,15], [1,10,4,11]) __ [2,11,7,15]
