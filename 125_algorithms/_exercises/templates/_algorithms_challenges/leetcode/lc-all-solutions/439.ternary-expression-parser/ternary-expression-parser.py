c_ Solution(o..
  ___ parseTernary  expression
    """
    :type expression: str
    :rtype: str
    """
    stack    # list
    i l..(expression) - 1
    w.... i >_ 0:
      __ expression[i] n.. __ ["?", ":"]:
        stack.a..(expression[i])
      ____ expression[i] __ "?":
        i -_ 1
        __ expression[i] __ "T":
          top stack.p.. )
          stack.p.. )
          stack.a..(top)
        ____ expression[i] __ "F":
          stack.p.. )
      i -_ 1
    r.. stack[0]
