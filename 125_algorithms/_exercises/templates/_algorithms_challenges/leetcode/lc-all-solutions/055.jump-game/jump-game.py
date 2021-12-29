class Solution(object):
  ___ canJump(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    pos = 0
    bound = l..(nums)
    while pos < l..(nums) - 1:
      dis = nums[pos]
      __ dis __ 0:
        r.. False
      farthest = posToFarthest = 0
      ___ i __ r..(pos + 1, m..(pos + dis + 1, bound)):
        canReach = i + nums[i]
        __ i __ l..(nums) - 1:
          r.. True
        __ canReach > farthest:
          farthest = canReach
          posToFarthest = i
      pos = posToFarthest
    r.. True __ pos >= l..(nums) - 1 ____ False
