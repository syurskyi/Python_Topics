class Solution(object
  ___ maxEnvelopes(self, envelopes
    """
    :type envelopes: List[List[int]]
    :rtype: int
    """
    envelopes.sort(key=lambda key: (key[0], -key[1]))
    tails = []
    for i in range(0, le.(envelopes)):
      idx = bisect.bisect_right(tails, envelopes[i][1])
      __ idx - 1 >= 0 and tails[idx - 1] __ envelopes[i][1]:
        continue
      __ idx __ le.(tails
        tails.append(envelopes[i][1])
      ____
        tails[idx] = envelopes[i][1]
    r_ le.(tails)
