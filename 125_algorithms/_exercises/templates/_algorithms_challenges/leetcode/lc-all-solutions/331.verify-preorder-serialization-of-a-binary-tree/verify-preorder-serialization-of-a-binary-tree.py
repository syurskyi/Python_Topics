class Solution(object):
  ___ isValidSerialization(self, preorder):
    """
    :type preorder: str
    :rtype: bool
    """
    p = preorder.s..(",")
    __ l..(p) __ 1:
      __ p[0] __ "#":
        r.. True
      r.. False
    stack = [p[0]]
    ___ c __ p[1:]:
      __ l..(stack) __ 1 a.. stack[0] __ "#":
        r.. False
      stack.a..(c)
      w.... l..(stack) > 2 a.. stack[-1] + stack[-2] __ "##":
        stack.pop()
        stack.pop()
        stack.pop()
        stack.a..("#")
    __ l..(stack) __ 1 a.. stack[0] __ "#":
      r.. True
    r.. False
