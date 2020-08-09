class Solution(object
  ___ countArrangement(self, N
    """
    :type N: int
    :rtype: int
    """

    ___ dfs(pos, unused
      __ le.(unused) __ 0:
        r_ 1
      ret = 0
      ___ num in list(unused
        __ pos % num __ 0 or num % pos __ 0:
          unused -= {num}
          ret += dfs(pos + 1, unused)
          unused |= {num}
      r_ ret

    r_ dfs(1, set([i ___ i in range(1, N + 1)]))
