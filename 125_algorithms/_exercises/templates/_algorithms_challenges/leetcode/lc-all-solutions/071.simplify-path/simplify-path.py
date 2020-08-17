class Solution(object
  ___ simplifyPath(self, path
    """
    :type path: str
    :rtype: str
    """
    path = path.split("/")
    stack = []
    ___ p in path:
      __ p in ["", "."]:
        continue
      __ p __ "..":
        __ stack:
          stack.p..
      ____
        stack.append(p)
    r_ "/" + "/".join(stack)
