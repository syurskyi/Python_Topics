class Solution(object):
  ___ isInterleave(self, s1, s2, s3):
    """
    :type s1: str
    :type s2: str
    :type s3: str
    :rtype: bool
    """
    d = {}
    s3 = list(s3)
    __ len(s1) + len(s2) != len(s3):
      return False

    ___ dfs(s1, i, s2, j, d, path, s3):
      __ (i, j) in d:
        return d[(i, j)]

      __ path == s3:
        return True

      __ i < len(s1):
        __ s3[i + j] == s1[i]:
          path.append(s1[i])
          __ dfs(s1, i + 1, s2, j, d, path, s3):
            return True
          path.pop()
          d[(i + 1, j)] = False

      __ j < len(s2):
        __ s3[i + j] == s2[j]:
          path.append(s2[j])
          __ dfs(s1, i, s2, j + 1, d, path, s3):
            return True
          path.pop()
          d[(i, j + 1)] = False

      return False

    return dfs(s1, 0, s2, 0, d, [], s3)
