"""
Your NumArray object will be instantiated and called as such:
obj = NumArray(nums)
param_1 = obj.sumRange(i,j)
"""


class NumArray:
    ___ __init__(self, nums
        """
        :type nums: List[int]
        """
        __ not nums:
            r_

        n = le.(nums)
        self.prefix_sum = [0] * (n + 1)

        ___ i __ range(1, n + 1
            self.prefix_sum[i] = self.prefix_sum[i - 1] + nums[i - 1]

    ___ sumRange(self, i, j
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        __ (
            not self.prefix_sum or
            i < 0 or
            j + 1 >= le.(self.prefix_sum)

            r_ 0
        r_ self.prefix_sum[j + 1] - self.prefix_sum[i]
