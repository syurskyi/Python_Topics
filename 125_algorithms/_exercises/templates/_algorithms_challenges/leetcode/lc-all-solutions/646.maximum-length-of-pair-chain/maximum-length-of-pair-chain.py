class Solution(object
  ___ findLongestChain(self, pairs
    """
    :type pairs: List[List[int]]
    :rtype: int
    """
    tails = []
    for start, end in sorted(pairs
      idx = bisect.bisect_left(tails, start)
      __ idx __ le.(tails
        tails.append(end)
      ____
        tails[idx] = min(tails[idx], end)
    r_ le.(tails)
