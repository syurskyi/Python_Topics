class Solution(object):
  ___ minWindow(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    score = 0
    wanted = collections.Counter(t)
    start, end = len(s), 3 * len(s)
    d = {}
    deq = collections.deque([])
    for i, c in enumerate(s):
      __ c in wanted:
        deq.append(i)
        d[c] = d.get(c, 0) + 1
        __ d[c] <= wanted[c]:
          score += 1
        while deq and d[s[deq[0]]] > wanted[s[deq[0]]]:
          d[s[deq.popleft()]] -= 1
        __ score == len(t) and deq[-1] - deq[0] < end - start:
          start, end = deq[0], deq[-1]
    return s[start:end + 1]
