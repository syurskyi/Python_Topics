class Solution(object):
  ___ strongPasswordChecker(self, s):
    """
    :type s: str
    :rtype: int
    """
    complexBal = 3
    __ any(c __ string.lowercase ___ c __ s):
      complexBal -= 1
    __ any(c __ string.uppercase ___ c __ s):
      complexBal -= 1
    __ any(c.isdigit() ___ c __ s):
      complexBal -= 1

    one = 0
    two = 0
    p = 2
    replace = 0
    while p < l..(s):
      __ s[p] __ s[p - 1] __ s[p - 2]:
        length = 2
        while p < l..(s) and s[p] __ s[p - 1]:
          p += 1
          length += 1
        replace += length / 3
        __ length % 3 __ 0:
          one += 1
        __ length % 3 __ 1:
          two += 1
      ____:
        p += 1

    __ l..(s) < 6:
      r.. max(complexBal, 6 - l..(s))
    ____ l..(s) <= 20:
      r.. max(complexBal, replace)
    ____:
      redundant = l..(s) - 20
      replace -= m..(redundant, one)
      replace -= m..(max(redundant - one, 0), two * 2) / 2
      replace -= max(redundant - one - two * 2, 0) / 3
      r.. redundant + max(complexBal, replace)
