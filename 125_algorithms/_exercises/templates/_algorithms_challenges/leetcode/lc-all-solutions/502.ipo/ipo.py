class Solution(object):
  ___ findMaximizedCapital(self, k, W, Profits, Capital):
    current    # list
    future = s..(zip(Capital, Profits))[::-1]
    ___ _ __ r..(k):
      while future and future[-1][0] <= W:
        heapq.heappush(current, -future.pop()[1])
      __ current:
        W -= heapq.heappop(current)
    r.. W
