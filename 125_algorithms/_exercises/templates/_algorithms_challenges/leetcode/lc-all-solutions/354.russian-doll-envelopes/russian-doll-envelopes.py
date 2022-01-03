c_ Solution(object):
  ___ maxEnvelopes(self, envelopes):
    """
    :type envelopes: List[List[int]]
    :rtype: int
    """
    envelopes.s..(key=l.... key: (key[0], -key[1]))
    tails    # list
    ___ i __ r..(0, l..(envelopes)):
      idx = bisect.bisect_right(tails, envelopes[i][1])
      __ idx - 1 >= 0 a.. tails[idx - 1] __ envelopes[i][1]:
        continue
      __ idx __ l..(tails):
        tails.a..(envelopes[i][1])
      ____:
        tails[idx] = envelopes[i][1]
    r.. l..(tails)
