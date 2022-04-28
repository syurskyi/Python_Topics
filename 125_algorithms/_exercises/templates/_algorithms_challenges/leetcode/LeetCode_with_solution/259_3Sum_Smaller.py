c_ Solution o..
    # def threeSumSmaller(self, nums, target):
    #     """
    #     :type nums: List[int]
    #     :type target: int
    #     :rtype: int
    #     """
    #     # https://leetcode.com/articles/3sum-smaller/#approach-2-binary-search-accepted
    #     nums.sort()
    #     ls = len(nums)
    #     res = 0
    #     for i in range(ls - 1):
    #         res += self.twoSumSmaller(nums, i + 1, target - nums[i])
    #     return res
    #
    # def twoSumSmaller(self, nums, start, target):
    #     res = 0
    #     for i in range(start, len(nums)):
    #         pos = self.binarySearch(nums, i, target - nums[i])
    #         res += pos - i
    #     return res
    #
    # def binarySearch(self, nums, start, target):
    #     left, right = start, len(nums) - 1
    #     while left < right:
    #         mid = (left + right + 1) / 2
    #         if nums[mid] < target:
    #             # left should always less than target
    #             left = mid
    #         else:
    #             right = mid - 1
    #     return left

    ___ threeSumSmaller  nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # https://leetcode.com/articles/3sum-smaller/#approach-2-binary-search-accepted
        nums.s..
        ls = l.. nums)
        res = 0
        ___ i __ r.. ls - 1):
            res += twoSumSmaller(nums, i + 1, target - nums[i])
        r_ res

    ___ twoSumSmaller  nums, start, target):
        res, left, right = 0, start, l.. nums) - 1
        w.. left < right:
            __ nums[left] + nums[right] < target:
                res += right - left
                left += 1
            ____
                right -= 1
        r_ res