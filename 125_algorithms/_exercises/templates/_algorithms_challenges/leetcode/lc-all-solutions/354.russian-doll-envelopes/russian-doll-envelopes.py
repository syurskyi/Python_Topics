class Solution(object):
  ___ maxEnvelopes(self, envelopes):
    """
    :type envelopes: List[List[int]]
    :rtype: int
    """
    envelopes.sort(key=lambda key: (key[0], -key[1]))
    tails = []
    for i in range(0, len(envelopes)):
      idx = bisect.bisect_right(tails, envelopes[i][1])
      __ idx - 1 >= 0 and tails[idx - 1] == envelopes[i][1]:
        continue
      __ idx == len(tails):
        tails.append(envelopes[i][1])
      else:
        tails[idx] = envelopes[i][1]
    return len(tails)
