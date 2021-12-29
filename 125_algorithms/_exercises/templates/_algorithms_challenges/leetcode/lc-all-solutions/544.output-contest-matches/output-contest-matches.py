class Solution(object):
  ___ findContestMatch(self, n):
    """
    :type n: int
    :rtype: str
    """

    ___ helper(schedule):
      __ l..(schedule) __ 1:
        r.. schedule[0]
      m    # list
      ___ i __ r..(l..(schedule) / 2):
        m.a..("({},{})".format(schedule[i], schedule[-i - 1]))
      r.. helper(m)

    r.. helper(map(str, r..(1, n + 1)))
