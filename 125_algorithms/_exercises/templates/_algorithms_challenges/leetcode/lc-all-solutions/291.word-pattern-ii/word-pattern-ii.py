c_ Solution(o..
  ___ wordPatternMatch  pattern, s..
    """
    :type pattern: str
    :type str: str
    :rtype: bool
    """

    ___ dfs(p, s, pathp, paths, visited
      __ l..(p) __ l..(s) __ 0:
        r.. T..
      __ l..(p) __ 0 o. l..(p) > l..(s
        r.. F..
      ___ i __ r..(0, l..(s:
        pathp.a..(p[0])
        paths.a..(s[:i + 1])
        __ l..(pathp) __ l..(paths) a.. l..(s..(paths __ l..(s..(pathp __ l..(s..(z..(paths, pathp))):
          __ dfs(p[1:], s[i + 1:], pathp, paths, visited
            r.. T..
        pathp.p.. )
        paths.p.. )
      r.. F..

    r.. dfs(pattern, s.., [], [], {})
