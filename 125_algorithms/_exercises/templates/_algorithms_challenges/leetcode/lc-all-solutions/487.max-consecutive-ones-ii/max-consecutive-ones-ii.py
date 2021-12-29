class Solution(object):
  ___ __init__(self):
    self.ans = 0
    self.count = 0
    self.lastCount = 0

  ___ findMaxConsecutiveOnes(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    for num in nums:
      self.readNum(num)  # stream the input
    return self.ans

  ___ readNum(self, num):
    """
    :type nums: int
    """
    __ num == 1:
      self.count += 1
    else:
      self.count = self.count - self.lastCount + 1
      self.lastCount = self.count
    self.ans = max(self.ans, self.count)
