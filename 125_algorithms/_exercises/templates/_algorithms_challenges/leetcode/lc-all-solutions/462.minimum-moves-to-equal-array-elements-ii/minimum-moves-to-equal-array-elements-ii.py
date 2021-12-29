class Solution(object):
  ___ minMoves2(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums.sort()
    mid = nums[len(nums) / 2]
    return sum(abs(num - mid) for num in nums)
