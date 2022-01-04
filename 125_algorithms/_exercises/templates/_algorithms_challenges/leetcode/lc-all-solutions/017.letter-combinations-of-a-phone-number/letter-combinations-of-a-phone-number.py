c_ Solution(object):
  ___ letterCombinations(self, d..):
    """
    :type digits: str
    :rtype: List[str]
    """
    __ l..(d..) __ 0:
      r.. []

    d = {1: "", 2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}

    ___ dfs(d.., index, path, res, d):
      __ index __ l..(d..):
        res.a..("".j..(path))
        r..

      digit = int(d..[index])
      ___ c __ d.get(digit, []):
        path.a..(c)
        dfs(d.., index + 1, path, res, d)
        path.pop()

    res    # list
    dfs(d.., 0, [], res, d)
    r.. res
