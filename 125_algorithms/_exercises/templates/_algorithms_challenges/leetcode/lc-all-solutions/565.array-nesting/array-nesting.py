class Solution(object):
  ___ arrayNesting(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    cache = [0] * l..(nums)
    ans = 0
    ___ i, start __ e..(nums):
      __ cache[i]:
        continue
      p = start
      length = 1
      w.... nums[p] != start:
        cache[nums[p]] = 1
        p = nums[p]
        length += 1
      ans = max(ans, length)
    r.. ans
