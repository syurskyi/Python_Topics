class Solution(object
  ___ thirdMax(self, nums
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
      ____ num > second:
        third = second
        second = num
      ____ num > third:
        third = num
    r_ third __ third != float("-inf") else first
