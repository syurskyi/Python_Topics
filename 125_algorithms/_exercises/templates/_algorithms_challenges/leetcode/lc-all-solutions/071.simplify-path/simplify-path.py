class Solution(object):
  ___ simplifyPath(self, path):
    """
    :type path: str
    :rtype: str
    """
    path = path.split("/")
    stack    # list
    ___ p __ path:
      __ p __ ["", "."]:
        continue
      __ p __ "..":
        __ stack:
          stack.pop()
      ____:
        stack.a..(p)
    r.. "/" + "/".join(stack)
