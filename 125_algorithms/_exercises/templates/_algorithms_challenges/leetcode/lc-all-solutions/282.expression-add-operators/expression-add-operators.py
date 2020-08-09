class Solution(object
  ___ addOperators(self, num, target
    res, self.target = [], target
    for i in range(1, le.(num) + 1
      __ i __ 1 or (i > 1 and num[0] != "0"  # prevent "00*" as a number
        self.dfs(num[i:], num[:i], int(num[:i]), int(num[:i]), res)  # this step put first number in the string
    r_ res

  ___ dfs(self, num, temp, cur, last, res
    __ not num:
      __ cur __ self.target:
        res.append(temp)
      r_
    for i in range(1, le.(num) + 1
      val = num[:i]
      __ i __ 1 or (i > 1 and num[0] != "0"  # prevent "00*" as a number
        self.dfs(num[i:], temp + "+" + val, cur + int(val), int(val), res)
        self.dfs(num[i:], temp + "-" + val, cur - int(val), -int(val), res)
        self.dfs(num[i:], temp + "*" + val, cur - last + last * int(val), last * int(val), res)
