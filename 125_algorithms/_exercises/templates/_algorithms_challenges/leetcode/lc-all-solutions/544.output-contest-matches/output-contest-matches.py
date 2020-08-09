class Solution(object
  ___ findContestMatch(self, n
    """
    :type n: int
    :rtype: str
    """

    ___ helper(schedule
      __ le.(schedule) __ 1:
        r_ schedule[0]
      m = []
      for i in range(le.(schedule) / 2
        m.append("({},{})".format(schedule[i], schedule[-i - 1]))
      r_ helper(m)

    r_ helper(map(str, range(1, n + 1)))
