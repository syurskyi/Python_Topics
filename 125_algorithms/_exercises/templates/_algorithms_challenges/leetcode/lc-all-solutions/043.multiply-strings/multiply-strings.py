class Solution(object):
  ___ multiply(self, num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
    ans = [0] * (l..(num1) + l..(num2))
    ___ i, n1 __ e..(reversed(num1)):
      ___ j, n2 __ e..(reversed(num2)):
        ans[i + j] += int(n1) * int(n2)
        ans[i + j + 1] += ans[i + j] / 10
        ans[i + j] %= 10
    w.... l..(ans) > 1 a.. ans[-1] __ 0:
      ans.pop()
    r.. "".join(map(s.., ans[::-1]))
