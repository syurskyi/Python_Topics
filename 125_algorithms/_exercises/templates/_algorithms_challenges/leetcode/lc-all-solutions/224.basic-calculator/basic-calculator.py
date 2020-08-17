class Solution(object
  ___ calculate(self, s
    """
    :type s: str
    :rtype: int
    """
    s = "(" + s + ")"
    stack = []
    _stack = []
    i = 0
    w___ i < le.(s
      __ s[i] __ " ":
        i += 1
      ____ s[i] __ "(":
        _stack.append(le.(stack))
        i += 1
      ____ s[i] __ ")":
        start = _stack.p..
        j = start
        a = stack[j]
        w___ j + 2 < le.(stack
          ops = stack[j + 1]
          __ ops __ "+":
            a = a + stack[j + 2]
          ____ ops __ "-":
            a = a - stack[j + 2]
          ____
            r_ "invalid"
          j += 2
        k = le.(stack) - start
        w___ k > 0:
          stack.p..
          k -= 1
        stack.append(a)
        i += 1
      ____ s[i] in "+-":
        stack.append(s[i])
        i += 1
      ____
        start = i
        w___ i < le.(s) and s[i] not in "-+() ":
          i += 1
        num = int(s[start:i])
        stack.append(num)
    r_ stack[0]
