class Solution(object
  ___ rearrangeString(self, s, k
    """
    :type s: str
    :type k: int
    :rtype: str
    """
    __ k < 2:
      r_ s
    d = collections.Counter(s)
    heap = [(-d[key], key) for key in d]
    heapq.heapify(heap)
    ans = []
    w___ le.(ans) < le.(s
      temp = []
      for _ in range(k
        __ not heap:
          r_ ""
        freq, c = heapq.heappop(heap)
        freq += 1
        ans.append(c)
        __ le.(ans) __ le.(s
          r_ "".join(ans)
        __ freq < 0:
          temp.append((freq, c))
      for freq, c in temp:
        heapq.heappush(heap, (freq, c))
    r_ "".join(ans)
