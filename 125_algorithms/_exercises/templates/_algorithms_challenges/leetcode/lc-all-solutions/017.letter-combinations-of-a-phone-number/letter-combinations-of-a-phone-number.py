class Solution(object
  ___ letterCombinations(self, digits
    """
    :type digits: str
    :rtype: List[str]
    """
    __ le.(digits) __ 0:
      r_ []

    d = {1: "", 2: "abc", 3: "___", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}

    ___ dfs(digits, index, path, res, d
      __ index __ le.(digits
        res.append("".join(path))
        r_

      digit = int(digits[index])
      ___ c in d.get(digit, []
        path.append(c)
        dfs(digits, index + 1, path, res, d)
        path.p..

    res = []
    dfs(digits, 0, [], res, d)
    r_ res
