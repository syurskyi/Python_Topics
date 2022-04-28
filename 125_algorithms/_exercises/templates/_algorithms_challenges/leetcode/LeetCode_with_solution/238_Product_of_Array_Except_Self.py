c_ Solution o..
    ___ productExceptSelf  nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [1] * l.. nums)
        ___ i __ r.. 1, l.. nums)):
            ans[i] = ans[i - 1] * nums[i - 1]
        right = 1
        ___ i __ r.. l.. nums) - 1, -1, -1):
            ans[i] *= right
            right *= nums[i]
        r_ ans
