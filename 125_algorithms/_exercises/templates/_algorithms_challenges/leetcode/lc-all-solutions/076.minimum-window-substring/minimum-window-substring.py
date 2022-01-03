c_ Solution(object):
  ___ minWindow(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    score = 0
    wanted = collections.Counter(t)
    start, end = l..(s), 3 * l..(s)
    d    # dict
    deq = collections.deque([])
    ___ i, c __ e..(s):
      __ c __ wanted:
        deq.a..(i)
        d[c] = d.get(c, 0) + 1
        __ d[c] <= wanted[c]:
          score += 1
        w.... deq a.. d[s[deq[0]]] > wanted[s[deq[0]]]:
          d[s[deq.popleft()]] -= 1
        __ score __ l..(t) a.. deq[-1] - deq[0] < end - start:
          start, end = deq[0], deq[-1]
    r.. s[start:end + 1]
