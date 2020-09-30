from collections ______ Counter


class Solution(object
  ___ getHint(self, secret, guess
    """
    :type secret: str
    :type guess: str
    :rtype: str
    """
    a = b = 0
    ds = Counter()
    dg = Counter()
    ___ i __ range(le.(secret)):
      s = secret[i]
      g = guess[i]
      __ secret[i] __ guess[i]:
        a += 1
      ____
        ds[s] += 1
        dg[g] += 1
        __ ds[g] > 0:
          b += 1
          dg[g] -= 1
          ds[g] -= 1
        __ dg[s] > 0:
          b += 1
          ds[s] -= 1
          dg[s] -= 1
    r_ "{}A{}B".format(a, b)
