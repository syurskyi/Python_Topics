#!/usr/bin/python3
"""
We define a harmonious array is an array where the difference between its
maximum value and its minimum value is exactly 1.

Now, given an integer array, you need to find the length of its longest
harmonious subsequence among all its possible subsequences.

Example 1:
Input: [1,3,2,2,5,2,3,7]
Output: 5

Explanation: The longest harmonious subsequence is [3,2,2,2,3].
Note: The length of the input array will not exceed 20,000.
"""
____ typing _______ List
____ collections _______ defaultdict


c_ Solution:
    ___ findLHS(self, nums: List[int]) -> int:
        """
        counter and iterate
        """
        counter = defaultdict(int)
        ___ n __ nums:
            counter[n] += 1

        ret = 0
        ___ k, v __ counter.i..:
            __ k + 1 __ counter:
                ret = max(ret, v + counter[k + 1])

        r.. ret
