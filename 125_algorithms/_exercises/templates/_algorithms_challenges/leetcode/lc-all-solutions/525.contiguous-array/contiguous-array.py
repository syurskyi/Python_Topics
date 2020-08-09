class Solution(object
  ___ findMaxLength(self, nums
    """
    :type nums: List[int]
    :rtype: int
    """
    d = {0: -1}
    count = ans = 0
    delta = {1: -1, 0: 1}
    ___ i in range(le.(nums)):
      count += delta.get(nums[i], 0)
      __ count in d:
        ans = max(ans, i - d[count])
      ____
        d[count] = i
    r_ ans
