class Solution(object
  ___ canJump(self, nums
    """
    :type nums: List[int]
    :rtype: int
    """
    pos = 0
    bound = le.(nums)
    w___ pos < le.(nums) - 1:
      dis = nums[pos]
      __ dis __ 0:
        r_ False
      farthest = posToFarthest = 0
      for i in range(pos + 1, min(pos + dis + 1, bound)):
        canReach = i + nums[i]
        __ i __ le.(nums) - 1:
          r_ True
        __ canReach > farthest:
          farthest = canReach
          posToFarthest = i
      pos = posToFarthest
    r_ True __ pos >= le.(nums) - 1 else False
