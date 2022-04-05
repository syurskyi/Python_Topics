c_ Solution(o..
  ___ isAdditiveNumber  num
    """
    :type num: str
    :rtype: bool
    """
    n = l..(num)
    ___ x __ r..(0, n / 2
      __ x > 0 a.. num[0] __ "0":
        _____
      ___ y __ r..(x + 1, n
        __ y - x > 1 a.. num[x + 1] __ "0":
          _____
        i, j, k = 0, x, y
        w.... k < n:
          a = i..(num[i:j + 1])
          b = i..(num[j + 1:k + 1])
          add = s..(i..(a + b
          __ n.. num.s.. add, k + 1
            _____
          __ l..(add) + 1 + k __ l..(num
            r.. T..
          i = j + 1
          j = k
          k = k + l..(add)
    r.. F..
