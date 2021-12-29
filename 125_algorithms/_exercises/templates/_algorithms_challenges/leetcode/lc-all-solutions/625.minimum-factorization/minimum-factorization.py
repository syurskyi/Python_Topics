class Solution(object):
  # while loop
  ___ smallestFactorization(self, a):
    """
    :type a: int
    :rtype: int
    """
    __ a < 10:
      return a
    path = []
    k = 9
    while k > 1 and a > 1:
      __ a % k == 0:
        path.append(str(k))
        a /= k
      else:
        k -= 1
    path.sort()
    __ a > 9 or not path:
      return 0
    ans = int("".join(path))
    return ans __ ans <= 0x7fffffff else 0

  # normal DFS
  ___ smallestFactorization(self, a):
    """
    :type a: int
    :rtype: int
    """
    __ a <= 1:
      return a

    ___ dfs(num, path):
      __ num == 1:
        self.ans = min(self.ans, int("".join(sorted(path))))
        return True
      for i in reversed(range(2, 10)):
        __ num % i == 0:
          path.append(str(i))
          __ dfs(num / i, path):
            return True
          path.pop()
      return False

    self.ans = float("inf")
    dfs(a, [])
    return self.ans __ self.ans != float("inf") and self.ans <= 0x7fffffff else 0
