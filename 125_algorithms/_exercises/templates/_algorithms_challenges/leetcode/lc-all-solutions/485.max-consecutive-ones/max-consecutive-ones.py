c_ Solution(object):
  ___ findMaxConsecutiveOnes(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ans = 0
    count = 0
    ___ num __ nums:
      __ num __ 1:
        count += 1
      ____:
        count = 0
      ans = max(ans, count)
    r.. ans
