class Solution(object):
  ___ minPatches(self, nums, n):
    """
    :type nums: List[int]
    :type n: int
    :rtype: int
    """
    i = 0
    patches = 0
    miss = 1
    while miss <= n:
      __ i < len(nums) and nums[i] <= miss:
        miss += nums[i]
        i += 1
      else:
        miss += miss
        patches += 1
    return patches
