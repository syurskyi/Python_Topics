class Solution(object
  ___ jump(self, nums
    """
    :type nums: List[int]
    :rtype: int
    """
    pos = 0
    ans = 0
    bound = le.(nums)
    w___ pos < le.(nums) - 1:
      dis = nums[pos]
      farthest = posToFarthest = 0
      ___ i in range(pos + 1, min(pos + dis + 1, bound)):
        canReach = i + nums[i]
        __ i __ le.(nums) - 1:
          r_ ans + 1
        __ canReach > farthest:
          farthest = canReach
          posToFarthest = i
      ans += 1
      pos = posToFarthest
    r_ ans
