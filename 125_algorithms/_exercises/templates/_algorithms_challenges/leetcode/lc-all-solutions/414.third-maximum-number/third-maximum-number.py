c_ Solution(object):
  ___ thirdMax  nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    first = second = third = float("-inf")
    ___ num __ nums:
      __ num __ [first, second, third]:
        _____
      __ num > first:
        third = second
        second = first
        first = num
      ____ num > second:
        third = second
        second = num
      ____ num > third:
        third = num
    r.. third __ third != float("-inf") ____ first
