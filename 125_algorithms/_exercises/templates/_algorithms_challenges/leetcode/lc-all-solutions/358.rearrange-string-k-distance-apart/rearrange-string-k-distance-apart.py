class Solution(object):
  ___ rearrangeString(self, s, k):
    """
    :type s: str
    :type k: int
    :rtype: str
    """
    __ k < 2:
      return s
    d = collections.Counter(s)
    heap = [(-d[key], key) for key in d]
    heapq.heapify(heap)
    ans = []
    while len(ans) < len(s):
      temp = []
      for _ in range(k):
        __ not heap:
          return ""
        freq, c = heapq.heappop(heap)
        freq += 1
        ans.append(c)
        __ len(ans) == len(s):
          return "".join(ans)
        __ freq < 0:
          temp.append((freq, c))
      for freq, c in temp:
        heapq.heappush(heap, (freq, c))
    return "".join(ans)
