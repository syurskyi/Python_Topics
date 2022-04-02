"""
Your NumArray object will be instantiated and called as such:
obj = NumArray(nums)
param_1 = obj.sumRange(i,j)
"""


c_ NumArray:
    ___ - , nums
        """
        :type nums: List[int]
        """
        __ n.. nums:
            r..

        n = l..(nums)
        prefix_sum = [0] * (n + 1)

        ___ i __ r..(1, n + 1
            prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]

    ___ sumRange  i, j
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        __ (
            n.. prefix_sum o.
            i < 0 o.
            j + 1 >= l..(prefix_sum)

            r.. 0
        r.. prefix_sum[j + 1] - prefix_sum[i]
