c_ Solution(object):
  # while loop
  ___ smallestFactorization(self, a):
    """
    :type a: int
    :rtype: int
    """
    __ a < 10:
      r.. a
    path    # list
    k = 9
    w.... k > 1 a.. a > 1:
      __ a % k __ 0:
        path.a..(s..(k))
        a /= k
      ____:
        k -= 1
    path.s..()
    __ a > 9 o. n.. path:
      r.. 0
    ans = i..("".j..(path))
    r.. ans __ ans <= 0x7fffffff ____ 0

  # normal DFS
  ___ smallestFactorization(self, a):
    """
    :type a: int
    :rtype: int
    """
    __ a <= 1:
      r.. a

    ___ dfs(num, path):
      __ num __ 1:
        ans = m..(ans, i..("".j..(s..(path))))
        r.. T..
      ___ i __ r..(r..(2, 10)):
        __ num % i __ 0:
          path.a..(s..(i))
          __ dfs(num / i, path):
            r.. T..
          path.pop()
      r.. F..

    ans = float("inf")
    dfs(a, [])
    r.. ans __ ans != float("inf") a.. ans <= 0x7fffffff ____ 0
