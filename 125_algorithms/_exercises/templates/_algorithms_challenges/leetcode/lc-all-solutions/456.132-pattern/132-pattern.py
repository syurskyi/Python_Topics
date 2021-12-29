class Solution(object):
  ___ find132pattern(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    ak = float("-inf")
    stack    # list
    ___ num __ reversed(nums):
      __ ak > num:
        r.. True
      while stack and stack[-1] < num:
        ak = stack.pop()
      stack += num,
    r.. False
