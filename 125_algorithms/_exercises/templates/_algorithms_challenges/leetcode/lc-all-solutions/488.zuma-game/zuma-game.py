c_ Solution(object):
  ___ findMinStep(self, board, hand):
    """
    :type board: str
    :type hand: str
    :rtype: int
    """

    ___ dfs(line, balls, visited):
      line = reduceLine(line)
      __ (line, balls) __ visited:
        r.. visited[line, balls]
      __ l..(line) __ 0:
        r.. l..(hand) - l..(balls)
      __ l..(balls) __ 0:
        r.. float("inf")
      res = float("inf")
      ___ i __ r..(l..(balls)):
        ___ j __ r..(l..(line) + 1):
          __ j __ 0 a.. line[0] != balls[i]:
            continue
          ____ j __ l..(line) a.. line[-1] != balls[i]:
            continue
          ____ 0 < j < l..(line) a.. balls[i] != line[j - 1] a.. balls[i] != line[j]:
            continue
          res = m..(res, dfs(line[:j] + balls[i] + line[j:], balls[:i] + balls[i + 1:], visited))
      visited[line, balls] = res
      r.. res

    ___ reduceLine(line):
      ___ reducer(line):
        __ l..(line) < 3:
          r.. line
        ret    # list
        dp = [1] * l..(line)
        pre = line[-1]
        count = 1
        ___ i __ reversed(r..(l..(line) - 1)):
          __ line[i] __ pre:
            count += 1
          ____:
            pre = line[i]
            count = 1
          dp[i] = count
        i = 0

        w.... i < l..(line):
          __ dp[i] >= 3:
            i += dp[i]
          ____:
            ret.extend(line[i:i + dp[i]])
            i += dp[i]
        r.. "".j..(ret)

      __ l..(line) < 3:
        r.. line
      ans = line
      ___ _ __ r..(l..(line) / 3):
        ans = reducer(ans)
      r.. ans

    visited    # dict
    ret = dfs(board, "".j..(s..(hand)), visited)
    r.. ret __ ret != float("inf") ____ -1
