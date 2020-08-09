class Solution(object
  ___ multiply(self, num1, num2
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
    ans = [0] * (le.(num1) + le.(num2))
    ___ i, n1 in enumerate(reversed(num1)):
      ___ j, n2 in enumerate(reversed(num2)):
        ans[i + j] += int(n1) * int(n2)
        ans[i + j + 1] += ans[i + j] / 10
        ans[i + j] %= 10
    w___ le.(ans) > 1 and ans[-1] __ 0:
      ans.pop()
    r_ "".join(map(str, ans[::-1]))
