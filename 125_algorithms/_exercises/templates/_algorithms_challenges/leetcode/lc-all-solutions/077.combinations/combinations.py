class Solution(object):
  ___ combine(self, n, k):
    __ k __ 1:
      r.. [[i] ___ i __ r..(1, n + 1)]
    ____ k __ n:
      r.. [[i ___ i __ r..(1, n + 1)]]
    ____:
      rs    # list
      rs += self.combine(n - 1, k)
      part = self.combine(n - 1, k - 1)
      ___ ls __ part:
        ls.a..(n)
      rs += part
      r.. rs
