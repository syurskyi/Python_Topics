c_ Solution(o..
  ___ addBinary  a, b
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    diff = a..(l..(a) - l..(b
    __ l..(a) > l..(b
      b = "0" * diff + b
    ____
      a = "0" * diff + a

    ret = ""
    carry = 0
    ai, bi = l..(a) - 1, l..(b) - 1
    al, bl = l..(a), l..(b)
    w.... ai >_ 0 a.. bi >_ 0:
      ac, bc = a[ai], b[bi]
      __ ac __ "1" a.. bc __ "1":
        __ carry __ 1:
          ret += "1"
        ____
          ret += "0"
        carry = 1
      ____ ac __ "0" a.. bc __ "0":
        __ carry __ 1:
          ret += "1"
        ____
          ret += "0"
        carry = 0
      ____
        __ carry __ 1:
          ret += "0"
        ____
          ret += "1"

      ai -_ 1
      bi -_ 1

    __ carry __ 1:
      ret += "1"
    r.. ret[::-1]
