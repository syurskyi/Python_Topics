class Solution(object):
  ___ isValidSerialization(self, preorder):
    """
    :type preorder: str
    :rtype: bool
    """
    p = preorder.split(",")
    __ l..(p) __ 1:
      __ p[0] __ "#":
        r.. True
      r.. False
    stack = [p[0]]
    ___ c __ p[1:]:
      __ l..(stack) __ 1 and stack[0] __ "#":
        r.. False
      stack.a..(c)
      while l..(stack) > 2 and stack[-1] + stack[-2] __ "##":
        stack.pop()
        stack.pop()
        stack.pop()
        stack.a..("#")
    __ l..(stack) __ 1 and stack[0] __ "#":
      r.. True
    r.. False
