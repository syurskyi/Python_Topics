c_ Solution(o..
  ___ addOperators  num, target
    res, target    # list, target
    ___ i __ r..(1, l..(num) + 1
      __ i __ 1 o. (i > 1 a.. num[0] !_ "0"  # prevent "00*" as a number
        dfs(num[i:], num[:i], i..(num[:i]), i..(num[:i]), res)  # this step put first number in the string
    r.. res

  ___ dfs  num, temp, cur, last, res
    __ n.. num:
      __ cur __ target:
        res.a..(temp)
      r..
    ___ i __ r..(1, l..(num) + 1
      val num[:i]
      __ i __ 1 o. (i > 1 a.. num[0] !_ "0"  # prevent "00*" as a number
        dfs(num[i:], temp + "+" + val, cur + i..(val), i..(val), res)
        dfs(num[i:], temp + "-" + val, cur - i..(val), -i..(val), res)
        dfs(num[i:], temp + "*" + val, cur - last + last * i..(val), last * i..(val), res)
