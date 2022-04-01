c_ Solution(o..):
  ___ thirdMax  nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    first = second = third = f__("-inf")
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
    r.. third __ third != f__("-inf") ____ first
