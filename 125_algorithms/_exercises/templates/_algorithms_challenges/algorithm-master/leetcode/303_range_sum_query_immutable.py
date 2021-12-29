"""
Your NumArray object will be instantiated and called as such:
obj = NumArray(nums)
param_1 = obj.sumRange(i,j)
"""


class NumArray:
    ___ __init__(self, nums):
        """
        :type nums: List[int]
        """
        __ n.. nums:
            r..

        n = l..(nums)
        self.prefix_sum = [0] * (n + 1)

        ___ i __ r..(1, n + 1):
            self.prefix_sum[i] = self.prefix_sum[i - 1] + nums[i - 1]

    ___ sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        __ (
            n.. self.prefix_sum o.
            i < 0 o.
            j + 1 >= l..(self.prefix_sum)
        ):
            r.. 0
        r.. self.prefix_sum[j + 1] - self.prefix_sum[i]
