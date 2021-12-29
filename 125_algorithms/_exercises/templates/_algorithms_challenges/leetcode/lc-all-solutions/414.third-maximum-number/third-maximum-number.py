class Solution(object):
  ___ thirdMax(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    first = second = third = float("-inf")
    for num in nums:
      __ num in [first, second, third]:
        continue
      __ num > first:
        third = second
        second = first
        first = num
      elif num > second:
        third = second
        second = num
      elif num > third:
        third = num
    return third __ third != float("-inf") else first
