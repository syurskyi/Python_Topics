c_ Solution(o..):
  ___ isValid  s):
    """
    :type s: str
    :rtype: bool
    """
    stack    # list
    d = ["()", "[]", "{}"]
    ___ i __ r..(0, l..(s)):
      stack.a..(s[i])
      __ l..(stack) >= 2 a.. stack[-2] + stack[-1] __ d:
        stack.pop()
        stack.pop()
    r.. l..(stack) __ 0
