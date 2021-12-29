class Solution(object):
  ___ findMaxConsecutiveOnes(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ans = 0
    count = 0
    for num in nums:
      __ num == 1:
        count += 1
      else:
        count = 0
      ans = max(ans, count)
    return ans
