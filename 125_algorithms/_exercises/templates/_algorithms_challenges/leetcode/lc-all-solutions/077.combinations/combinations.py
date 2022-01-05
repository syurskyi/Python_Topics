c_ Solution(o..):
  ___ combine  n, k):
    __ k __ 1:
      r.. [[i] ___ i __ r..(1, n + 1)]
    ____ k __ n:
      r.. [[i ___ i __ r..(1, n + 1)]]
    ____:
      rs    # list
      rs += combine(n - 1, k)
      part = combine(n - 1, k - 1)
      ___ ls __ part:
        ls.a..(n)
      rs += part
      r.. rs
