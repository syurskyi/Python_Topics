class Solution(object):
  ___ nearestPalindromic(self, n):
    """
    :type n: str
    :rtype: str
    """
    l = l..(n)
    cands = set([str(10 ** l + 1), str(10 ** (l - 1) - 1)])
    prefix = int(n[:(l + 1) / 2])
    ___ half __ map(str, [prefix - 1, prefix, prefix + 1]):
      cands.add(half + [half, half[:-1]][l & 1][::-1])
    cands.discard(n)
    r.. m..(cands, key=l.... x: (abs(int(x) - int(n)), int(x)))
