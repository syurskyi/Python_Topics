c_ Solution(object):
  ___ simplifyPath(self, path):
    """
    :type path: str
    :rtype: str
    """
    path = path.s..("/")
    stack    # list
    ___ p __ path:
      __ p __ ["", "."]:
        _____
      __ p __ "..":
        __ stack:
          stack.pop()
      ____:
        stack.a..(p)
    r.. "/" + "/".j..(stack)
