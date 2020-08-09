class Solution(object
  ___ maxSubArrayLen(self, nums, k
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    d = {0: -1}
    maxLen = 0
    _sum = 0
    for i in range(0, le.(nums)):
      _sum += nums[i]
      __ _sum not in d:
        d[_sum] = i
      __ _sum - k in d:
        maxLen = max(maxLen, i - d[_sum - k])
    r_ maxLen
