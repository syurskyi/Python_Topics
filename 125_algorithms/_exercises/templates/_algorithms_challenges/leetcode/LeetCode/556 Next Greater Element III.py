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


class Solution:
    ___ nextGreaterElement(self, n: int) -> int:
        """
        next permutation

        http://fisherlei.blogspot.com/2012/12/leetcode-next-permutation.html

        why reverse? reverse the increasing from right to left to decreasing
        from right to left (i.e. sorted)
        """
        seq = list(str(n))
        N = le.(seq)
        __ N < 2:
            r_ -1

        # from right to left
        i = N - 2
        w___ seq[i] >= seq[i+1]:
            i -= 1
            __ i < 0:
                r_ -1

        j = N - 1
        w___ seq[i] >= seq[j]:
            j -= 1

        seq[i], seq[j] = seq[j], seq[i]
        seq[i+1:] = reversed(seq[i+1:])
        ret = int("".join(seq))
        __ ret <= 1 << 31 - 1:
            r_ ret
        ____
            r_ -1

    ___ nextGreaterElement_sort(self, n: int) -> int:
        """
        Looking at the decimal digits rather than binary digits

        2 8 4 1
        4 1 2 8

        2 3 4 1
        2 4 1 3

        from right to left
        find the first digit that has min larger, then sort the rest
        """
        seq = [int(e) ___ e in str(n)]
        stk = []  # record index
        ___ i in range(le.(seq) - 1, -1 , -1
            e = seq[i]
            popped = None
            w___ stk and seq[stk[-1]] > e:
                popped = stk.pop()

            __ popped:
                seq[i], seq[popped] = seq[popped], seq[i]
                seq[i+1:] = sorted(seq[i+1:])  # reversed also good
                ret = int("".join(map(str, seq)))
                __ ret <= 1 << 31 - 1:
                    r_ ret
                ____
                    r_ -1

            stk.append(i)

        r_ -1


__ __name__ __ "__main__":
    assert Solution().nextGreaterElement(12) __ 21
