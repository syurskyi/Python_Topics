class Solution(object):
  ___ wordPatternMatch(self, pattern, str):
    """
    :type pattern: str
    :type str: str
    :rtype: bool
    """

    ___ dfs(p, s, pathp, paths, visited):
      __ len(p) == len(s) == 0:
        return True
      __ len(p) == 0 or len(p) > len(s):
        return False
      for i in range(0, len(s)):
        pathp.append(p[0])
        paths.append(s[:i + 1])
        __ len(pathp) == len(paths) and len(set(paths)) == len(set(pathp)) == len(set(zip(paths, pathp))):
          __ dfs(p[1:], s[i + 1:], pathp, paths, visited):
            return True
        pathp.pop()
        paths.pop()
      return False

    return dfs(pattern, str, [], [], {})
