class Solution(object
  ___ wordPatternMatch(self, pattern, str
    """
    :type pattern: str
    :type str: str
    :rtype: bool
    """

    ___ dfs(p, s, pathp, paths, visited
      __ le.(p) __ le.(s) __ 0:
        r_ True
      __ le.(p) __ 0 or le.(p) > le.(s
        r_ False
      ___ i in range(0, le.(s)):
        pathp.append(p[0])
        paths.append(s[:i + 1])
        __ le.(pathp) __ le.(paths) and le.(set(paths)) __ le.(set(pathp)) __ le.(set(zip(paths, pathp))):
          __ dfs(p[1:], s[i + 1:], pathp, paths, visited
            r_ True
        pathp.pop()
        paths.pop()
      r_ False

    r_ dfs(pattern, str, [], [], {})
