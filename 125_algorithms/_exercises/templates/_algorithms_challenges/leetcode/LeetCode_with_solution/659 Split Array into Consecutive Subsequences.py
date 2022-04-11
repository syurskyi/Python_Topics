#!/usr/bin/python3
"""
You are given an integer array sorted in ascending order (may contain
duplicates), you need to split them into several subsequences, where each
subsequences consist of at least 3 consecutive integers. Return whether you can
make such a split.

Example 1:
Input: [1,2,3,3,4,5]
Output: True
Explanation:
You can split them into two consecutive subsequences :
1, 2, 3
3, 4, 5
Example 2:
Input: [1,2,3,3,4,4,5,5]
Output: True
Explanation:
You can split them into two consecutive subsequences :
1, 2, 3, 4, 5
3, 4, 5
Example 3:
Input: [1,2,3,4,4,5]
Output: False
Note:
The length of the input is in range of [1, 10000]
"""
____ t___ _______ L..
____ c.. _______ d..
_______ heapq


c_ Solution:
    ___ isPossible  nums: L..[i..]) __ b..:
        """
        Attribute a number to a existing consecutive subsequences
        future numbers depend on this number to form the subsequence can also
        attribtue to this existing subsequence

        If no existing one to attribtue, form a consecutive (l >= 3) by use the
        subsequent numbers by looking forward

        Let F[i] be the number of consecutive subsequence at A[i]
        """
        counter d..(i..)
        ___ e __ nums:
            counter[e] += 1

        F d..(i..)
        ___ e __ nums:
            __ counter[e] __ 0:
                _____
            counter[e] -_ 1

            __ F[e - 1] > 0:
                F[e - 1] -_ 1
                F[e] += 1
            ____ counter[e + 1] > 0 a.. counter[e + 2] > 0:
                F[e + 2] += 1
                counter[e + 1] -_ 1
                counter[e + 2] -_ 1
            ____
                r.. F..

        r.. T..

            
c_ Interval:
    ___ - , end, length
        end end
        length length

    ___ __lt__  other
        __ end __ other.end:
            r.. length < other.length

        r.. end < other.end

    ___  -r
        r.. r.. ((end, length


c_ Solution2:
    ___ isPossible  nums: L..[i..]) __ b..:
        """
        (length, last)
        heap sortest first
        >= 3, then drop

        split when duplicate
        """
        h    # list
        ___ n __ nums:
            w.... h a.. h[0].end + 1 < n:
                itvl heapq.heappop(h)
                __ itvl.length < 3:
                    r.. F..

            __ n.. h:
                heapq.heappush(h, Interval(n, 1
            ____ h[0].end + 1 __ n:
                itvl heapq.heappop(h)
                heapq.heappush(h, Interval(n, itvl.length + 1
            ____  # n == end
                heapq.heappush(h, Interval(n, 1


        ___ itvl __ h:
            __ itvl.length < 3:
                r.. F..

        r.. T..

__ _______ __ _______
    ... Solution().isPossible([1,2,3,3,4,5]) __ T..
    ... Solution().isPossible([1,2,3,3,4,4,5,5]) __ T..
    ... Solution().isPossible([1,2,3,4,4,5]) __ F..
