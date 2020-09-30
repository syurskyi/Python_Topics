class Solution(object
  ___ isInterleave(self, s1, s2, s3
    """
    :type s1: str
    :type s2: str
    :type s3: str
    :rtype: bool
    """
    d = {}
    s3 = list(s3)
    __ le.(s1) + le.(s2) != le.(s3
      r_ False

    ___ dfs(s1, i, s2, j, d, path, s3
      __ (i, j) __ d:
        r_ d[(i, j)]

      __ path __ s3:
        r_ True

      __ i < le.(s1
        __ s3[i + j] __ s1[i]:
          path.append(s1[i])
          __ dfs(s1, i + 1, s2, j, d, path, s3
            r_ True
          path.p..
          d[(i + 1, j)] = False

      __ j < le.(s2
        __ s3[i + j] __ s2[j]:
          path.append(s2[j])
          __ dfs(s1, i, s2, j + 1, d, path, s3
            r_ True
          path.p..
          d[(i, j + 1)] = False

      r_ False

    r_ dfs(s1, 0, s2, 0, d,   # list, s3)
