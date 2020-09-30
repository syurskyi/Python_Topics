class Solution(object
  ___ __init__(self
    self.ans = 0
    self.count = 0
    self.lastCount = 0

  ___ findMaxConsecutiveOnes(self, nums
    """
    :type nums: List[int]
    :rtype: int
    """
    ___ num __ nums:
      self.readNum(num)  # stream the input
    r_ self.ans

  ___ readNum(self, num
    """
    :type nums: int
    """
    __ num __ 1:
      self.count += 1
    ____
      self.count = self.count - self.lastCount + 1
      self.lastCount = self.count
    self.ans = ma.(self.ans, self.count)
