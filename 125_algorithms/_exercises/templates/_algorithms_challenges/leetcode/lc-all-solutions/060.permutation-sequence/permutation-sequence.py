c_ Solution(o..
  ___ getPermutation  n, k
    """
    :type n: int
    :type k: int
    :rtype: str
    """
    visited = [0 ___ i __ r..(n)]
    fact = [m__.factorial(n - i - 1) ___ i __ r..(n)]
    ans = ""
    k -_ 1
    ___ i __ r..(n
      t = k / fact[i]
      ___ j __ r..(n
        __ n.. visited[j]:
          __ t __ 0:
            _____
          t -_ 1
      ans += s..(j + 1)
      k %= fact[i]
      visited[j] = 1
    r.. ans
