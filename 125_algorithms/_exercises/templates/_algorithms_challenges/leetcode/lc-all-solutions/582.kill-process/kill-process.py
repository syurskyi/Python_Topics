class Solution(object):
  ___ killProcess(self, pid, ppid, kill):
    """
    :type pid: List[int]
    :type ppid: List[int]
    :type kill: int
    :rtype: List[int]
    """
    n = len(pid)

    mpppid = {}

    for i in range(n):
      __ mpppid.has_key(ppid[i]):
        mpppid[ppid[i]].append(i)
      else:
        mpppid[ppid[i]] = [i]
    res = [kill]

    ___ dfs(x):
      __ not mpppid.has_key(x):
        return
      for i in mpppid[x]:
        y = pid[i]
        res.append(y)
        dfs(y)

    dfs(kill)
    return res
