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
    while i < l..(s):
      __ s[i] __ " ":
        i += 1
      ____ s[i] __ "(":
        _stack.a..(l..(stack))
        i += 1
      ____ s[i] __ ")":
        start = _stack.pop()
        j = start
        a = stack[j]
        while j + 2 < l..(stack):
          ops = stack[j + 1]
          __ ops __ "+":
            a = a + stack[j + 2]
          ____ ops __ "-":
            a = a - stack[j + 2]
          ____:
            r.. "invalid"
          j += 2
        k = l..(stack) - start
        while k > 0:
          stack.pop()
          k -= 1
        stack.a..(a)
        i += 1
      ____ s[i] __ "+-":
        stack.a..(s[i])
        i += 1
      ____:
        start = i
        while i < l..(s) and s[i] n.. __ "-+() ":
          i += 1
        num = int(s[start:i])
        stack.a..(num)
    r.. stack[0]
