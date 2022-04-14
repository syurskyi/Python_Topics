#!/usr/bin/python3
"""
Alice and Bob have candy bars of different sizes: A[i] is the size of the i-th
bar of candy that Alice has, and B[j] is the size of the j-th bar of candy that
Bob has.

Since they are friends, they would like to exchange one candy bar each so that
after the exchange, they both have the same total amount of candy.  (The total
amount of candy a person has is the sum of the sizes of candy bars they have.)

Return an integer array ans where ans[0] is the size of the candy bar that Alice
must exchange, and ans[1] is the size of the candy bar that Bob must exchange.

If there are multiple answers, you may return any one of them.  It is guaranteed
an answer exists.

Example 1:

Input: A = [1,1], B = [2,2]
Output: [1,2]
Example 2:

Input: A = [1,2], B = [2,3]
Output: [1,2]
Example 3:

Input: A = [2], B = [1,3]
Output: [2,3]
Example 4:

Input: A = [1,2,5], B = [2,4]
Output: [5,4]

Note:

1 <= A.length <= 10000
1 <= B.length <= 10000
1 <= A[i] <= 100000
1 <= B[i] <= 100000
It is guaranteed that Alice and Bob have different total amounts of candy.
It is guaranteed there exists an answer.
"""
____ t___ _______ L..
_______ b__


c_ Solution:
    ___ fairCandySwap  A: L..[i..], B: L.. i.. __ L.. i..
        """
        It is a search problem. Use set as search.
        """
        sum_A s..(A)
        sum_B s..(B)
        diff (sum_B - sum_A) // 2  # it can be negative or positive
        set_B s..(B)
        ___ a __ A:
            __ a + diff __ set_B:
                r.. [a, a + diff]
                
        r..

    ___ fairCandySwap_complex  A: L..[i..], B: L.. i.. __ L.. i..
        """
        sum, to figure out the target O(N)
        exchange one
        exchange is (sum - target) + constant
        it is a search problem
        """
        sum_A s..(A)
        sum_B s..(B)
        __ sum_A > sum_B:
            r.. fairCandySwap(B, A)[::-1]

        A.s..()
        B.s..()
        diff (sum_B - sum_A) // 2
        ___ a __ A:
            i b__.bisect_left(B, a + diff)
            __ i < l..(B) a.. B[i] __ a + diff:
                r.. [a, a + diff]

        r..
