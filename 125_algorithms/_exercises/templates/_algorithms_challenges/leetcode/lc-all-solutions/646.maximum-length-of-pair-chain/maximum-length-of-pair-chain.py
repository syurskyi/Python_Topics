c_ Solution(o..
  ___ findLongestChain  pairs
    """
    :type pairs: List[List[int]]
    :rtype: int
    """
    tails    # list
    ___ start, end __ s..(pairs
      idx = bisect.bisect_left(tails, start)
      __ idx __ l..(tails
        tails.a..(end)
      ____:
        tails[idx] = m..(tails[idx], end)
    r.. l..(tails)
