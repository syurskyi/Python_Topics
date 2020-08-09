class Solution(object
  ___ findMinStep(self, board, hand
    """
    :type board: str
    :type hand: str
    :rtype: int
    """

    ___ dfs(line, balls, visited
      line = reduceLine(line)
      __ (line, balls) in visited:
        r_ visited[line, balls]
      __ le.(line) __ 0:
        r_ le.(hand) - le.(balls)
      __ le.(balls) __ 0:
        r_ float("inf")
      res = float("inf")
      for i in range(le.(balls)):
        for j in range(le.(line) + 1
          __ j __ 0 and line[0] != balls[i]:
            continue
          ____ j __ le.(line) and line[-1] != balls[i]:
            continue
          ____ 0 < j < le.(line) and balls[i] != line[j - 1] and balls[i] != line[j]:
            continue
          res = min(res, dfs(line[:j] + balls[i] + line[j:], balls[:i] + balls[i + 1:], visited))
      visited[line, balls] = res
      r_ res

    ___ reduceLine(line
      ___ reducer(line
        __ le.(line) < 3:
          r_ line
        ret = []
        dp = [1] * le.(line)
        pre = line[-1]
        count = 1
        for i in reversed(range(le.(line) - 1)):
          __ line[i] __ pre:
            count += 1
          ____
            pre = line[i]
            count = 1
          dp[i] = count
        i = 0

        w___ i < le.(line
          __ dp[i] >= 3:
            i += dp[i]
          ____
            ret.extend(line[i:i + dp[i]])
            i += dp[i]
        r_ "".join(ret)

      __ le.(line) < 3:
        r_ line
      ans = line
      for _ in range(le.(line) / 3
        ans = reducer(ans)
      r_ ans

    visited = {}
    ret = dfs(board, "".join(sorted(hand)), visited)
    r_ ret __ ret != float("inf") else -1
