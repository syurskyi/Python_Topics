class Solution(object
  ___ findMaximizedCapital(self, k, W, Profits, Capital
    current = []
    future = sorted(zip(Capital, Profits))[::-1]
    ___ _ in range(k
      w___ future and future[-1][0] <= W:
        heapq.heappush(current, -future.p..[1])
      __ current:
        W -= heapq.heappop(current)
    r_ W
