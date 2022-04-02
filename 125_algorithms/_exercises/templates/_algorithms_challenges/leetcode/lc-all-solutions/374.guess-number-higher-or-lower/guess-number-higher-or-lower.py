# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

c_ Solution(o..
  ___ guessNumber  n
    """
    :type n: int
    :rtype: int
    """
    l, r = 1, n
    w.... l < r:
      m = l + (r - l) / 2
      g = guess(m)
      __ g __ -1:
        r = m - 1
      ____ g __ 1:
        l = m + 1
      ____:
        r.. m
    r.. l
