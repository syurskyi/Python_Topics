class Solution(object
  ___ addStrings(self, num1, num2
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
    carry = 0
    i = le.(num1) - 1
    j = le.(num2) - 1
    ans = ""
    ___ k in reversed(range(0, max(le.(num1), le.(num2)))):
      a = int(num1[i]) __ i >= 0 else 0
      b = int(num2[j]) __ j >= 0 else 0
      i, j = i - 1, j - 1
      c = carry
      carry = 0
      su. = a + b + c
      __ su. >= 10:
        carry = 1
        ans += str(su. - 10)
      ____
        ans += str(su.)
    __ carry __ 1:
      ans += "1"
    r_ ans[::-1]
