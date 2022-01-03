c_ Solution(object):
  ___ parseTernary(self, expression):
    """
    :type expression: str
    :rtype: str
    """
    stack    # list
    i = l..(expression) - 1
    w.... i >= 0:
      __ expression[i] n.. __ ["?", ":"]:
        stack.a..(expression[i])
      ____ expression[i] __ "?":
        i -= 1
        __ expression[i] __ "T":
          top = stack.pop()
          stack.pop()
          stack.a..(top)
        ____ expression[i] __ "F":
          stack.pop()
      i -= 1
    r.. stack[0]
