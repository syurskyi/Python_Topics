c_ Solution(o..
  ___ findMaximizedCapital  k, W, Profits, Capital
    current    # list
    future = s..(z..(Capital, Profits))[::-1]
    ___ _ __ r..(k
      w.... future a.. future[-1][0] <= W:
        heapq.heappush(current, -future.pop()[1])
      __ current:
        W -= heapq.heappop(current)
    r.. W
