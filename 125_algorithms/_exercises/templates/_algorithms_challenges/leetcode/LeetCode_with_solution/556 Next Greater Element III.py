#!/usr/bin/python3
"""
Given a positive 32-bit integer n, you need to find the smallest 32-bit integer
which has exactly the same digits existing in the integer n and is greater in
value than n. If no such positive 32-bit integer exists, you need to return -1.

Example 1:

Input: 12
Output: 21


Example 2:

Input: 21
Output: -1
"""


c_ Solution:
    ___ nextGreaterElement  n: i.. __ i..
        """
        next permutation

        http://fisherlei.blogspot.com/2012/12/leetcode-next-permutation.html

        why reverse? reverse the increasing from right to left to decreasing
        from right to left (i.e. sorted)
        """
        seq l..(s..(n
        N l..(seq)
        __ N < 2:
            r.. -1

        # from right to left
        i N - 2
        w.... seq[i] >_ seq[i+1]:
            i -_ 1
            __ i < 0:
                r.. -1

        j N - 1
        w.... seq[i] >_ seq[j]:
            j -_ 1

        seq[i], seq[j] seq[j], seq[i]
        seq[i+1:] r..(seq[i+1:])
        ret i..("".j..(seq
        __ ret <_ 1 << 31 - 1:
            r.. ret
        ____
            r.. -1

    ___ nextGreaterElement_sort  n: i.. __ i..
        """
        Looking at the decimal digits rather than binary digits

        2 8 4 1
        4 1 2 8

        2 3 4 1
        2 4 1 3

        from right to left
        find the first digit that has min larger, then sort the rest
        """
        seq [i..(e) ___ e __ s..(n)]
        stk    # list  # record index
        ___ i __ r..(l..(seq) - 1, -1 , -1
            e seq[i]
            popped N..
            w.... stk a.. seq[stk[-1]] > e:
                popped stk.p.. )

            __ popped:
                seq[i], seq[popped] seq[popped], seq[i]
                seq[i+1:] s..(seq[i+1:])  # reversed also good
                ret i..("".j.. m..(s.., seq)))
                __ ret <_ 1 << 31 - 1:
                    r.. ret
                ____
                    r.. -1

            stk.a..(i)

        r.. -1


__ _______ __ _______
    ... Solution().nextGreaterElement(12) __ 21
