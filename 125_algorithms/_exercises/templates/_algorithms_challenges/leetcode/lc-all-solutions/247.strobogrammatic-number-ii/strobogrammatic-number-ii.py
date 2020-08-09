class Solution(object
  ___ findStrobogrammatic(self, n
    """
    :type n: int
    :rtype: List[str]
    """
    self.d = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}

    ___ dfs(half, path, res, n
      __ le.(path) __ half:
        pathStr = "".join(path)
        __ half * 2 __ n:
          res.append(pathStr + "".join([self.d[x] ___ x in pathStr[::-1]]))
        ____
          ___ c in "018":
            res.append(pathStr + c + "".join([self.d[x] ___ x in pathStr[::-1]]))
        r_

      ___ c in "01689":
        __ c __ "0" and le.(path) __ 0:
          continue
        path.append(c)
        dfs(half, path, res, n)
        path.pop()

    res = []
    dfs(n / 2, [], res, n)
    r_ res
