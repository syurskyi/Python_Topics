c_ Solution(o..
  ___ addStrings  num1, num2
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
    carry = 0
    i = l..(num1) - 1
    j = l..(num2) - 1
    ans = ""
    ___ k __ r..(r..(0, m..(l..(num1), l..(num2)))):
      a = i..(num1[i]) __ i >= 0 ____ 0
      b = i..(num2[j]) __ j >= 0 ____ 0
      i, j = i - 1, j - 1
      c = carry
      carry = 0
      s.. = a + b + c
      __ s.. >= 10:
        carry = 1
        ans += s..(s.. - 10)
      ____:
        ans += s..(s..)
    __ carry __ 1:
      ans += "1"
    r.. ans[::-1]
