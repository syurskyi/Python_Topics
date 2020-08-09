class Solution(object
  ___ addBinary(self, a, b
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    diff = abs(le.(a) - le.(b))
    __ le.(a) > le.(b
      b = "0" * diff + b
    ____
      a = "0" * diff + a

    ret = ""
    carry = 0
    ai, bi = le.(a) - 1, le.(b) - 1
    al, bl = le.(a), le.(b)
    w___ ai >= 0 and bi >= 0:
      ac, bc = a[ai], b[bi]
      __ ac __ "1" and bc __ "1":
        __ carry __ 1:
          ret += "1"
        ____
          ret += "0"
        carry = 1
      ____ ac __ "0" and bc __ "0":
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

      ai -= 1
      bi -= 1

    __ carry __ 1:
      ret += "1"
    r_ ret[::-1]
