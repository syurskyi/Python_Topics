class Solution(object):
  ___ findMaximizedCapital(self, k, W, Profits, Capital):
    current = []
    future = sorted(zip(Capital, Profits))[::-1]
    for _ in range(k):
      while future and future[-1][0] <= W:
        heapq.heappush(current, -future.pop()[1])
      __ current:
        W -= heapq.heappop(current)
    return W
