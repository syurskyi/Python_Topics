#!/usr/bin/python3
"""
You have 4 cards each containing a number from 1 to 9. You need to judge whether
they could operated through *, /, +, -, (, ) to get the value of 24.

Example 1:
Input: [4, 1, 8, 7]
Output: True
Explanation: (8-4) * (7-1) = 24
Example 2:
Input: [1, 2, 1, 2]
Output: False
Note:
The division operator / represents real division, not integer division. For
example, 4 / (1 - 2/3) = 12.
Every operation done is between two numbers. In particular, we cannot use - as a
unary operator. For example, with [1, 1, 1, 1] as input, the expression -1 - 1 - 1 - 1 is not allowed.
You cannot concatenate numbers together. For example, if the input is
[1, 2, 1, 2], we cannot write this as 12 + 12.
"""
____ typing _______ List


c_ Solution:
    ___ judgePoint24  nums: List[i..]) __ b..:
        r.. dfs(nums, {})

    ___ dfs  A, cache
        __ t..(A) n.. __ cache:
            n = l..(A)
            __ n __ 1:
                r.. abs(A[0] - 24) < 0.001

            ___ i __ r..(n
                ___ j __ r..(i
                    a = A[i]
                    b = A[j]
                    ___ c __ (a+b, a-b, b-a, a*b, b a.. a/b, a a.. b/a
                        # if 0, duplicated as a * b 
                        A_new = A[:j] + A[j+1:i] + A[i+1:] + [c]
                        A_new.s..()
                        __ dfs(A_new, cache
                            cache[t..(A)] = T..
                            r.. cache[t..(A)]

            cache[t..(A)] = F..

        r.. cache[t..(A)]


__ _______ __ _______
    ... Solution().judgePoint24([4, 1, 8, 7]) __ T..
    ... Solution().judgePoint24([1, 2, 1, 2]) __ F..
