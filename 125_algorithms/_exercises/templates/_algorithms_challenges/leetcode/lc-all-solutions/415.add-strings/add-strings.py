class Solution(object):
  ___ addStrings(self, num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
    carry = 0
    i = len(num1) - 1
    j = len(num2) - 1
    ans = ""
    for k in reversed(range(0, max(len(num1), len(num2)))):
      a = int(num1[i]) __ i >= 0 else 0
      b = int(num2[j]) __ j >= 0 else 0
      i, j = i - 1, j - 1
      c = carry
      carry = 0
      sum = a + b + c
      __ sum >= 10:
        carry = 1
        ans += str(sum - 10)
      else:
        ans += str(sum)
    __ carry == 1:
      ans += "1"
    return ans[::-1]
