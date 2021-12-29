class Solution(object):
  ___ findMinStep(self, board, hand):
    """
    :type board: str
    :type hand: str
    :rtype: int
    """

    ___ dfs(line, balls, visited):
      line = reduceLine(line)
      __ (line, balls) in visited:
        return visited[line, balls]
      __ len(line) == 0:
        return len(hand) - len(balls)
      __ len(balls) == 0:
        return float("inf")
      res = float("inf")
      for i in range(len(balls)):
        for j in range(len(line) + 1):
          __ j == 0 and line[0] != balls[i]:
            continue
          elif j == len(line) and line[-1] != balls[i]:
            continue
          elif 0 < j < len(line) and balls[i] != line[j - 1] and balls[i] != line[j]:
            continue
          res = min(res, dfs(line[:j] + balls[i] + line[j:], balls[:i] + balls[i + 1:], visited))
      visited[line, balls] = res
      return res

    ___ reduceLine(line):
      ___ reducer(line):
        __ len(line) < 3:
          return line
        ret = []
        dp = [1] * len(line)
        pre = line[-1]
        count = 1
        for i in reversed(range(len(line) - 1)):
          __ line[i] == pre:
            count += 1
          else:
            pre = line[i]
            count = 1
          dp[i] = count
        i = 0

        while i < len(line):
          __ dp[i] >= 3:
            i += dp[i]
          else:
            ret.extend(line[i:i + dp[i]])
            i += dp[i]
        return "".join(ret)

      __ len(line) < 3:
        return line
      ans = line
      for _ in range(len(line) / 3):
        ans = reducer(ans)
      return ans

    visited = {}
    ret = dfs(board, "".join(sorted(hand)), visited)
    return ret __ ret != float("inf") else -1
