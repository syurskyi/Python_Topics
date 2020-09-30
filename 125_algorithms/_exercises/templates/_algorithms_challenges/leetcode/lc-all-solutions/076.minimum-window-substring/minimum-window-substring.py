class Solution(object
  ___ minWindow(self, s, t
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    score = 0
    wanted = collections.Counter(t)
    start, end = le.(s), 3 * le.(s)
    d = {}
    deq = collections.deque(  # list)
    ___ i, c __ enumerate(s
      __ c __ wanted:
        deq.append(i)
        d[c] = d.get(c, 0) + 1
        __ d[c] <= wanted[c]:
          score += 1
        w___ deq and d[s[deq[0]]] > wanted[s[deq[0]]]:
          d[s[deq.popleft()]] -= 1
        __ score __ le.(t) and deq[-1] - deq[0] < end - start:
          start, end = deq[0], deq[-1]
    r_ s[start:end + 1]
