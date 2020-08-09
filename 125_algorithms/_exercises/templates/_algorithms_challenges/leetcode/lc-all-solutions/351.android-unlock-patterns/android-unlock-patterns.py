class Solution(object
  ___ numberOfPatterns(self, m, n
    """
    :type m: int
    :type n: int
    :rtype: int
    """

    ___ dfs(m, n, prev, visited, length
      __ m <= length <= n:
        self.ans += 1

      __ length __ n:
        r_

      ___ i in range(1, 10
        __ i not in visited:
          x, y, xp, yp = (i - 1) / 3, (i - 1) % 3, (prev - 1) / 3, (prev - 1) % 3
          __ (5 not in visited and (x + xp, y + yp) __ (2, 2)) or (
            (x __ xp and abs(y - yp) __ 2) or (y __ yp and abs(x - xp) __ 2)) and (prev + i) / 2 not in visited:
            continue
          visited |= {i}
          dfs(m, n, i, visited, length + 1)
          visited.discard(i)

    visited = set()
    self.ans = 0
    dfs(m, n, -99, visited, 0)
    r_ self.ans
