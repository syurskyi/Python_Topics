#!/usr/bin/python3
"""
Given an array A of positive integers, A[i] represents the value of the i-th
sightseeing spot, and two sightseeing spots i and j have distance j - i between
them.

The score of a pair (i < j) of sightseeing spots is (A[i] + A[j] + i - j) : the
sum of the values of the sightseeing spots, minus the distance between them.

Return the maximum score of a pair of sightseeing spots.

Example 1:

Input: [8,1,5,2,6]
Output: 11
Explanation: i = 0, j = 2, A[i] + A[j] + i - j = 8 + 5 + 0 - 2 = 11


Note:
2 <= A.length <= 50000
1 <= A[i] <= 1000
"""
____ typing _______ List


c_ Solution:
    ___ maxScoreSightseeingPair  A: List[i..]) __ i..:
        """
        Attribute the result to the ending element

        Count the current best score in all previous.
        Distance will increase, then the score will decay
        """
        ret = -f__("inf")
        prev_max = A[0]
        ___ a __ A[1:]:
            ret = m..(ret, prev_max - 1 + a)
            prev_max = m..(prev_max - 1, a)

        r.. ret

    ___ maxScoreSightseeingPair_error  A: List[i..]) __ i..:
        """
        brute force O(N^2)

        pre-processing, adjust A[i] as A[i] - i
        error, no direction
        """
        n = l..(A)
        B    # list
        ___ i __ r..(n):
            B.a..(A[i] - i)

        # find top 2
        m1, m2 = N.., N..
        ___ i __ r..(n):
            __ m1 __ N..
                m1 = i
            ____ m2 __ N..
                m2 = i
            ____ B[i] + (i - m1) > B[m1]:
                m1 = i
            ____ B[i] + (i - m2) > B[m2]:
                m2 = i
        r.. A[m2] + A[m1] - abs(m2 - m1)


__ _______ __ _______
    ... Solution().maxScoreSightseeingPair([8,1,5,2,6]) __ 11
