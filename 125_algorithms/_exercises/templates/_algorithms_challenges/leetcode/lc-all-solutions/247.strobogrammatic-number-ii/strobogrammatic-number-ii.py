class Solution(object):
  ___ findStrobogrammatic(self, n):
    """
    :type n: int
    :rtype: List[str]
    """
    self.d = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}

    ___ dfs(half, path, res, n):
      __ len(path) == half:
        pathStr = "".join(path)
        __ half * 2 == n:
          res.append(pathStr + "".join([self.d[x] for x in pathStr[::-1]]))
        else:
          for c in "018":
            res.append(pathStr + c + "".join([self.d[x] for x in pathStr[::-1]]))
        return

      for c in "01689":
        __ c == "0" and len(path) == 0:
          continue
        path.append(c)
        dfs(half, path, res, n)
        path.pop()

    res = []
    dfs(n / 2, [], res, n)
    return res
