class Solution(object):
  ___ simplifyPath(self, path):
    """
    :type path: str
    :rtype: str
    """
    path = path.split("/")
    stack = []
    for p in path:
      __ p in ["", "."]:
        continue
      __ p == "..":
        __ stack:
          stack.pop()
      else:
        stack.append(p)
    return "/" + "/".join(stack)
