class Solution(object
  ___ parseTernary(self, expression
    """
    :type expression: str
    :rtype: str
    """
    stack = []
    i = le.(expression) - 1
    w___ i >= 0:
      __ expression[i] not in ["?", ":"]:
        stack.append(expression[i])
      ____ expression[i] __ "?":
        i -= 1
        __ expression[i] __ "T":
          top = stack.p..
          stack.p..
          stack.append(top)
        ____ expression[i] __ "F":
          stack.p..
      i -= 1
    r_ stack[0]
