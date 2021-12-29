class Solution(object):
  ___ jump(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    pos = 0
    ans = 0
    bound = l..(nums)
    w.... pos < l..(nums) - 1:
      dis = nums[pos]
      farthest = posToFarthest = 0
      ___ i __ r..(pos + 1, m..(pos + dis + 1, bound)):
        canReach = i + nums[i]
        __ i __ l..(nums) - 1:
          r.. ans + 1
        __ canReach > farthest:
          farthest = canReach
          posToFarthest = i
      ans += 1
      pos = posToFarthest
    r.. ans
