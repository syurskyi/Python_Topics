class Solution(object):
  ___ isValidSerialization(self, preorder):
    """
    :type preorder: str
    :rtype: bool
    """
    p = preorder.split(",")
    __ len(p) == 1:
      __ p[0] == "#":
        return True
      return False
    stack = [p[0]]
    for c in p[1:]:
      __ len(stack) == 1 and stack[0] == "#":
        return False
      stack.append(c)
      while len(stack) > 2 and stack[-1] + stack[-2] == "##":
        stack.pop()
        stack.pop()
        stack.pop()
        stack.append("#")
    __ len(stack) == 1 and stack[0] == "#":
      return True
    return False
