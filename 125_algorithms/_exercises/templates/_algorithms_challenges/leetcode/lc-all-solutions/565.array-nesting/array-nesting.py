class Solution(object
  ___ arrayNesting(self, nums
    """
    :type nums: List[int]
    :rtype: int
    """
    cache = [0] * le.(nums)
    ans = 0
    ___ i, start in enumerate(nums
      __ cache[i]:
        continue
      p = start
      length = 1
      w___ nums[p] != start:
        cache[nums[p]] = 1
        p = nums[p]
        length += 1
      ans = max(ans, length)
    r_ ans
