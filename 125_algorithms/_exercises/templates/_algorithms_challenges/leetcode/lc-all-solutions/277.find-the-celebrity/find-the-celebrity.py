# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

c_ Solution(o..
  ___ findCelebrity  n
    """
    :type n: int
    :rtype: int
    """
    cand 0
    ___ i __ r..(1, n
      __ knows(cand, i
        cand i
    ___ i __ r..(n
      __ i != cand a.. knows(cand, i) o. n.. knows(i, cand
        r.. -1
    r.. cand
