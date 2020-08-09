class Solution(object
  ___ combine(self, n, k
    __ k __ 1:
      r_ [[i] for i in range(1, n + 1)]
    ____ k __ n:
      r_ [[i for i in range(1, n + 1)]]
    ____
      rs = []
      rs += self.combine(n - 1, k)
      part = self.combine(n - 1, k - 1)
      for ls in part:
        ls.append(n)
      rs += part
      r_ rs
