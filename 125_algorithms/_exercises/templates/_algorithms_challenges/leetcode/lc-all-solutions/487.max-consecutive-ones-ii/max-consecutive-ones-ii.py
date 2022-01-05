c_ Solution(o..):
  ___ - ):
    ans = 0
    count = 0
    lastCount = 0

  ___ findMaxConsecutiveOnes  nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ___ num __ nums:
      readNum(num)  # stream the input
    r.. ans

  ___ readNum  num):
    """
    :type nums: int
    """
    __ num __ 1:
      count += 1
    ____:
      count = count - lastCount + 1
      lastCount = count
    ans = m..(ans, count)
