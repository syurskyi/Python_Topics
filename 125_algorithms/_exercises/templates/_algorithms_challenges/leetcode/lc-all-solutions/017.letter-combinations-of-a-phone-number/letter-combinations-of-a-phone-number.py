c_ Solution(object):
  ___ letterCombinations(self, digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    __ l..(digits) __ 0:
      r.. []

    d = {1: "", 2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}

    ___ dfs(digits, index, path, res, d):
      __ index __ l..(digits):
        res.a..("".j..(path))
        r..

      digit = int(digits[index])
      ___ c __ d.get(digit, []):
        path.a..(c)
        dfs(digits, index + 1, path, res, d)
        path.pop()

    res    # list
    dfs(digits, 0, [], res, d)
    r.. res
