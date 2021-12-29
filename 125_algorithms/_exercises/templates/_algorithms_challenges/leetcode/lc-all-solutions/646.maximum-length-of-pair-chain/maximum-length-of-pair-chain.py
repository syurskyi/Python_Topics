class Solution(object):
  ___ findLongestChain(self, pairs):
    """
    :type pairs: List[List[int]]
    :rtype: int
    """
    tails = []
    for start, end in sorted(pairs):
      idx = bisect.bisect_left(tails, start)
      __ idx == len(tails):
        tails.append(end)
      else:
        tails[idx] = min(tails[idx], end)
    return len(tails)
