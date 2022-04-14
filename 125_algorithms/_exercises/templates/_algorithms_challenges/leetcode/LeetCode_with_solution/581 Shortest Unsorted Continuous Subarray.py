#!/usr/bin/python3
"""
Given an integer array, you need to find one continuous subarray that if you
only sort this subarray in ascending order, then the whole array will be sorted
in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the
whole array sorted in ascending order.

Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.
"""
____ t___ _______ L..


c_ Solution:
    ___ findUnsortedSubarray  nums: L.. i.. __ i..
        """
        Sorted at both ends
        Then search for the two ends by nums[i+1] > nums[i] on the left side
        (right side similar)

        Problem: may over-include, consider  1 2 5 9 4 6 ...
        need to shrink from 1 2 5 9 to 1 2 according to min value

        nums[lo - 1] <= min && max <= nums[hi + 1]
        """
        n l..(nums)
        lo, hi 0, n - 1
        w.... lo < hi a.. nums[lo] <_ nums[lo + 1]:
            lo += 1

        w.... lo < hi a.. nums[hi - 1] <_ nums[hi]:
            hi -_ 1

        __ hi <_ lo:
            r.. 0

        mini f__('inf')
        maxa -f__('inf')
        ___ i __ r..(lo, hi + 1
            mini m..(mini, nums[i])
            maxa m..(maxa, nums[i])

        w.... lo - 1 >_ 0 a.. nums[lo - 1] > mini:
            lo -_ 1
        w.... hi + 1 < n a.. nums[hi + 1] < maxa:
            hi += 1

        r.. hi - lo + 1

    ___ findUnsortedSubarray_sort  nums: L.. i.. __ i..
        """
        Brute force sort and compare O(n lgn)
        """
        e.. l..(s..(nums
        i 0
        w.... i < l..(nums) a.. nums[i] __ e..[i]:
            i += 1

        j l..(nums) - 1
        w.... j >_ i a.. nums[j] __ e..[j]:
            j -_ 1

        r.. j - i + 1


__ _______ __ _______
    ... Solution().findUnsortedSubarray([2, 1]) __ 2
    ... Solution().findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]) __ 5
