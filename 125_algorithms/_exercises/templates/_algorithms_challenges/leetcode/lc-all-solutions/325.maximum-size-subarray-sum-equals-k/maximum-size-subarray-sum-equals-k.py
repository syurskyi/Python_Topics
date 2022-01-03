c_ Solution(object):
  ___ maxSubArrayLen(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    d = {0: -1}
    maxLen = 0
    _sum = 0
    ___ i __ r..(0, l..(nums)):
      _sum += nums[i]
      __ _sum n.. __ d:
        d[_sum] = i
      __ _sum - k __ d:
        maxLen = max(maxLen, i - d[_sum - k])
    r.. maxLen
