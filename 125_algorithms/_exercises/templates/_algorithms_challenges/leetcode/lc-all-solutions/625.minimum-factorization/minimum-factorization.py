c_ Solution(o..
  # while loop
  ___ smallestFactorization  a
    """
    :type a: int
    :rtype: int
    """
    __ a < 10:
      r.. a
    p..    # list
    k = 9
    w.... k > 1 a.. a > 1:
      __ a % k __ 0:
        p...a..(s..(k))
        a /= k
      ____:
        k -= 1
    p...s..()
    __ a > 9 o. n.. p..:
      r.. 0
    ans = i..("".j..(p..))
    r.. ans __ ans <= 0x7fffffff ____ 0

  # normal DFS
  ___ smallestFactorization  a
    """
    :type a: int
    :rtype: int
    """
    __ a <= 1:
      r.. a

    ___ dfs(num, p..
      __ num __ 1:
        ans = m..(ans, i..("".j..(s..(p..))))
        r.. T..
      ___ i __ r..(r..(2, 10)):
        __ num % i __ 0:
          p...a..(s..(i))
          __ dfs(num / i, p..
            r.. T..
          p...pop()
      r.. F..

    ans = f__("inf")
    dfs(a, [])
    r.. ans __ ans != f__("inf") a.. ans <= 0x7fffffff ____ 0
