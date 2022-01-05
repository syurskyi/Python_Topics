c_ Solution(o..):
  ___ simplifyPath  path):
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
