class Solution(object
  # w___ loop
  ___ smallestFactorization(self, a
    """
    :type a: int
    :rtype: int
    """
    __ a < 10:
      r_ a
    path = []
    k = 9
    w___ k > 1 and a > 1:
      __ a % k __ 0:
        path.append(str(k))
        a /= k
      ____
        k -= 1
    path.sort()
    __ a > 9 or not path:
      r_ 0
    ans = int("".join(path))
    r_ ans __ ans <= 0x7fffffff else 0

  # normal DFS
  ___ smallestFactorization(self, a
    """
    :type a: int
    :rtype: int
    """
    __ a <= 1:
      r_ a

    ___ dfs(num, path
      __ num __ 1:
        self.ans = min(self.ans, int("".join(sorted(path))))
        r_ True
      ___ i in reversed(range(2, 10)):
        __ num % i __ 0:
          path.append(str(i))
          __ dfs(num / i, path
            r_ True
          path.pop()
      r_ False

    self.ans = float("inf")
    dfs(a, [])
    r_ self.ans __ self.ans != float("inf") and self.ans <= 0x7fffffff else 0
