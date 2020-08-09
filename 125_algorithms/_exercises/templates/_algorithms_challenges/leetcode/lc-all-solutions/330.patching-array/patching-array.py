class Solution(object
  ___ minPatches(self, nums, n
    """
    :type nums: List[int]
    :type n: int
    :rtype: int
    """
    i = 0
    patches = 0
    miss = 1
    w___ miss <= n:
      __ i < le.(nums) and nums[i] <= miss:
        miss += nums[i]
        i += 1
      ____
        miss += miss
        patches += 1
    r_ patches
