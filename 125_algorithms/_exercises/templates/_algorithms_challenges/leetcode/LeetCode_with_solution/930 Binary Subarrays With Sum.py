#!/usr/bin/python3
"""
In an array A of 0s and 1s, how many non-empty subarrays have sum S?

Example 1:

Input: A = [1,0,1,0,1], S = 2
Output: 4
Explanation:
The 4 subarrays are bolded below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]


Note:

A.length <= 30000
0 <= S <= A.length
A[i] is either 0 or 1.
"""
____ t___ _______ L..


c_ Solution:
    ___ numSubarraysWithSum  A: L..[i..], S: i..) __ i..:
        """
        Two pointers
        i_lo and i_hi
        count = i_hi - i_lo + 1
        """
        ret 0
        i_lo, i_hi, j 0, 0, 0
        sum_lo, sum_hi 0, 0
        ___ j __ r..(l..(A:
            sum_lo += A[j]
            sum_hi += A[j]
            w.... i_lo < j a.. sum_lo > S:
                sum_lo -_ A[i_lo]
                i_lo += 1
            w.... i_hi < j a.. (sum_hi > S o. sum_hi __ S a.. A[i_hi] __ 0
                sum_hi -_ A[i_hi]
                i_hi += 1
            ... i_hi >_ i_lo
            __ sum_lo __ S:
                ... sum_hi __ S
                ret += i_hi - i_lo + 1

        r.. ret

    ___ numSubarraysWithSum_error  A: L..[i..], S: i..) __ i..:
        """
        Continuous subarrays sum using prefix sum to target O(N), space O(N)
        Two pointer, O(N), space O(1)
        """
        ret 0
        i 0
        j 0
        n l..(A)
        cur_sum 0
        w.... j < n:
            cur_sum += A[j]
            __ cur_sum < S a.. j < n:
                j += 1
            ____ cur_sum __ S:
                ret += 1
                w.... i <_ j a.. A[i] __ 0:
                    i += 1
                    ret += 1
                j += 1
            ____
                w.... i <_ j a.. cur_sum > S:
                    cur_sum -_ A[i]
                    i += 1
                __ cur_sum __ S:
                    ret += 1
                    w.... i <_ j a.. A[i] __ 0:
                        i += 1
                        ret += 1
                j += 1

        r.. ret


__ _______ __ _______
    ... Solution().numSubarraysWithSum([1,0,1,0,1], 2) __ 4
