c_ NumArray o..
    ___ -  nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        res = [0] * (l.. nums) + 1)
        data = list(nums)
        ___ i __ r.. l.. data)):
            res[i + 1] = res[i] + nums[i]

    ___ sumRange  i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        r_ res[j + 1] - res[i]

        # Your NumArray object will be instantiated and called as such:
        # numArray = NumArray(nums)
        # numArray.sumRange(0, 1)
        # numArray.sumRange(1, 2)