class Solution(object):
  ___ removeDuplicateLetters(self, s):
    """
    :type s: str
    :rtype: str
    """
    d = {}
    count = {}
    ___ c __ s:
      d[c] = d.get(c, 0) + 1
      count[c] = count.get(c, 0) + 1
    stack    # list
    cache = set()
    ___ c __ s:
      __ c n.. __ cache:
        w.... stack a.. stack[-1] > c a.. d[stack[-1]] > 1 a.. d[stack[-1]] != 1 a.. count[stack[-1]] > 0:
          cache.discard(stack.pop())
        stack.a..(c)
        cache.add(c)
      count[c] -= 1
    r.. "".join(stack)
