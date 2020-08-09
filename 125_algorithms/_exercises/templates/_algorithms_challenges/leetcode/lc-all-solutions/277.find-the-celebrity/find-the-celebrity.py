# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# ___ knows(a, b

class Solution(object
  ___ findCelebrity(self, n
    """
    :type n: int
    :rtype: int
    """
    cand = 0
    ___ i in range(1, n
      __ knows(cand, i
        cand = i
    ___ i in range(n
      __ i != cand and knows(cand, i) or not knows(i, cand
        r_ -1
    r_ cand
