class Solution:
    ___ findMissing(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        __ not nums:
            return 0

        ans = n = len(nums)

        for i in range(n):
            ans ^= i ^ nums[i]

        return ans


class Solution:
    ___ findMissing(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        __ not nums:
            return 0

        nums.sort()

        for i in range(len(nums)):
            __ i != nums[i]:
                return i

        return i + 1
