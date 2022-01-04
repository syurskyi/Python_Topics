c_ Solution(object):
  ___ multiply(self, num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
    ans = [0] * (l..(num1) + l..(num2))
    ___ i, n1 __ e..(r..(num1)):
      ___ j, n2 __ e..(r..(num2)):
        ans[i + j] += i..(n1) * i..(n2)
        ans[i + j + 1] += ans[i + j] / 10
        ans[i + j] %= 10
    w.... l..(ans) > 1 a.. ans[-1] __ 0:
      ans.pop()
    r.. "".j..(map(s.., ans[::-1]))
