class Solution(object
  ___ isValidSerialization(self, preorder
    """
    :type preorder: str
    :rtype: bool
    """
    p = preorder.split(",")
    __ le.(p) __ 1:
      __ p[0] __ "#":
        r_ True
      r_ False
    stack = [p[0]]
    for c in p[1:]:
      __ le.(stack) __ 1 and stack[0] __ "#":
        r_ False
      stack.append(c)
      w___ le.(stack) > 2 and stack[-1] + stack[-2] __ "##":
        stack.pop()
        stack.pop()
        stack.pop()
        stack.append("#")
    __ le.(stack) __ 1 and stack[0] __ "#":
      r_ True
    r_ False
