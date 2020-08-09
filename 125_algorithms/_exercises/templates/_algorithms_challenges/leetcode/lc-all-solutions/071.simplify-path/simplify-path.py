class Solution(object
  ___ simplifyPath(self, path
    """
    :type path: str
    :rtype: str
    """
    path = path.split("/")
    stack = []
    for p in path:
      __ p in ["", "."]:
        continue
      __ p __ "..":
        __ stack:
          stack.pop()
      ____
        stack.append(p)
    r_ "/" + "/".join(stack)
