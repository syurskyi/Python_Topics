c_ Solution(o..
  ___ isInterleave  s1, s2, s3
    """
    :type s1: str
    :type s2: str
    :type s3: str
    :rtype: bool
    """
    d    # dict
    s3 = l..(s3)
    __ l..(s1) + l..(s2) != l..(s3
      r.. F..

    ___ dfs(s1, i, s2, j, d, p.., s3
      __ (i, j) __ d:
        r.. d[(i, j)]

      __ p.. __ s3:
        r.. T..

      __ i < l..(s1
        __ s3[i + j] __ s1[i]:
          p...a..(s1[i])
          __ dfs(s1, i + 1, s2, j, d, p.., s3
            r.. T..
          p...pop()
          d[(i + 1, j)] = F..

      __ j < l..(s2
        __ s3[i + j] __ s2[j]:
          p...a..(s2[j])
          __ dfs(s1, i, s2, j + 1, d, p.., s3
            r.. T..
          p...pop()
          d[(i, j + 1)] = F..

      r.. F..

    r.. dfs(s1, 0, s2, 0, d, [], s3)
