____ collections _______ Counter


class Solution(object):
  ___ findContentChildren(self, children, cookies):
    """
    :type g: List[int]
    :type s: List[int]
    :rtype: int
    """
    cookies.sort()
    children.sort()
    i = 0
    ___ cookie __ cookies:
      __ i >= l..(children):
        break
      __ children[i] <= cookie:
        i += 1
    r.. i
