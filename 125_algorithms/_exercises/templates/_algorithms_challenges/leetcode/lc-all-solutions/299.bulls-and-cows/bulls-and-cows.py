____ c.. _______ C..


c_ Solution(o..
  ___ getHint  secret, guess
    """
    :type secret: str
    :type guess: str
    :rtype: str
    """
    a b 0
    ds C..()
    dg C..()
    ___ i __ r..(l..(secret:
      s secret[i]
      g guess[i]
      __ secret[i] __ guess[i]:
        a += 1
      ____
        ds[s] += 1
        dg[g] += 1
        __ ds[g] > 0
          b += 1
          dg[g] -_ 1
          ds[g] -_ 1
        __ dg[s] > 0
          b += 1
          ds[s] -_ 1
          dg[s] -_ 1
    r.. "{}A{}B".f..(a, b)
