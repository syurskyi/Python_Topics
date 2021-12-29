class Solution(object):
  ___ findMaxLength(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    d = {0: -1}
    count = ans = 0
    delta = {1: -1, 0: 1}
    ___ i __ r..(l..(nums)):
      count += delta.get(nums[i], 0)
      __ count __ d:
        ans = max(ans, i - d[count])
      ____:
        d[count] = i
    r.. ans
