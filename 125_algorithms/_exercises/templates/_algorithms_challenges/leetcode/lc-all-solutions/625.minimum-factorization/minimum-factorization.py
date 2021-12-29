class Solution(object):
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
    while k > 1 and a > 1:
      __ a % k __ 0:
        path.a..(s..(k))
        a /= k
      ____:
        k -= 1
    path.sort()
    __ a > 9 o. n.. path:
      r.. 0
    ans = int("".join(path))
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
        self.ans = m..(self.ans, int("".join(s..(path))))
        r.. True
      ___ i __ reversed(r..(2, 10)):
        __ num % i __ 0:
          path.a..(s..(i))
          __ dfs(num / i, path):
            r.. True
          path.pop()
      r.. False

    self.ans = float("inf")
    dfs(a, [])
    r.. self.ans __ self.ans != float("inf") and self.ans <= 0x7fffffff ____ 0
