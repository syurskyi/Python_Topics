from collections import Counter


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
    for cookie in cookies:
      __ i >= len(children):
        break
      __ children[i] <= cookie:
        i += 1
    return i
