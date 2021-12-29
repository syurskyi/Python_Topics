class Solution(object):
  ___ checkPerfectNumber(self, num):
    """
    :type num: int
    :rtype: bool
    """
    ans = 1
    div = 2
    while div ** 2 <= num:
      __ num % div __ 0:
        ans += div
        ans += num / div
      div += 1
    r.. ans __ num __ num != 1 ____ False
