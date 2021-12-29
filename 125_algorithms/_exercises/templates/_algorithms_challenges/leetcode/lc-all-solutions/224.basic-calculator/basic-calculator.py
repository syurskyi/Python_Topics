class Solution(object):
  ___ calculate(self, s):
    """
    :type s: str
    :rtype: int
    """
    s = "(" + s + ")"
    stack    # list
    _stack    # list
    i = 0
    w.... i < l..(s):
      __ s[i] __ " ":
        i += 1
      ____ s[i] __ "(":
        _stack.a..(l..(stack))
        i += 1
      ____ s[i] __ ")":
        start = _stack.pop()
        j = start
        a = stack[j]
        w.... j + 2 < l..(stack):
          ops = stack[j + 1]
          __ ops __ "+":
            a = a + stack[j + 2]
          ____ ops __ "-":
            a = a - stack[j + 2]
          ____:
            r.. "invalid"
          j += 2
        k = l..(stack) - start
        w.... k > 0:
          stack.pop()
          k -= 1
        stack.a..(a)
        i += 1
      ____ s[i] __ "+-":
        stack.a..(s[i])
        i += 1
      ____:
        start = i
        w.... i < l..(s) a.. s[i] n.. __ "-+() ":
          i += 1
        num = int(s[start:i])
        stack.a..(num)
    r.. stack[0]
