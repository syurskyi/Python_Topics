c_ Solution(o..
  ___ strongPasswordChecker  s
    """
    :type s: str
    :rtype: int
    """
    complexBal 3
    __ a__(c __ s__.lowercase ___ c __ s
      complexBal -_ 1
    __ a__(c __ s__.uppercase ___ c __ s
      complexBal -_ 1
    __ a__(c.i.. ___ c __ s
      complexBal -_ 1

    one 0
    two 0
    p 2
    r.. 0
    w.... p < l..(s
      __ s[p] __ s[p - 1] __ s[p - 2]:
        length 2
        w.... p < l..(s) a.. s[p] __ s[p - 1]:
          p += 1
          length += 1
        r.. += length / 3
        __ length % 3 __ 0:
          one += 1
        __ length % 3 __ 1:
          two += 1
      ____
        p += 1

    __ l..(s) < 6:
      r.. m..(complexBal, 6 - l..(s
    ____ l..(s) <_ 20:
      r.. m..(complexBal, r..)
    ____
      redundant l..(s) - 20
      r.. -_ m..(redundant, one)
      r.. -_ m..(m..(redundant - one, 0), two * 2) / 2
      r.. -_ m..(redundant - one - two * 2, 0) / 3
      r.. redundant + m..(complexBal, r..)
