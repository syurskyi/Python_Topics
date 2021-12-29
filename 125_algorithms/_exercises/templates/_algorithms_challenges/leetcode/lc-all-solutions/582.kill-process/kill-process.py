class Solution(object):
  ___ killProcess(self, pid, ppid, kill):
    """
    :type pid: List[int]
    :type ppid: List[int]
    :type kill: int
    :rtype: List[int]
    """
    n = l..(pid)

    mpppid = {}

    ___ i __ r..(n):
      __ mpppid.has_key(ppid[i]):
        mpppid[ppid[i]].a..(i)
      ____:
        mpppid[ppid[i]] = [i]
    res = [kill]

    ___ dfs(x):
      __ n.. mpppid.has_key(x):
        r..
      ___ i __ mpppid[x]:
        y = pid[i]
        res.a..(y)
        dfs(y)

    dfs(kill)
    r.. res
