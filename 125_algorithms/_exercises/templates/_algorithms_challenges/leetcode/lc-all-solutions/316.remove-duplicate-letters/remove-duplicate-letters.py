class Solution(object
  ___ removeDuplicateLetters(self, s
    """
    :type s: str
    :rtype: str
    """
    d = {}
    count = {}
    ___ c __ s:
      d[c] = d.get(c, 0) + 1
      count[c] = count.get(c, 0) + 1
    stack =   # list
    cache = set()
    ___ c __ s:
      __ c not __ cache:
        w___ stack and stack[-1] > c and d[stack[-1]] > 1 and d[stack[-1]] != 1 and count[stack[-1]] > 0:
          cache.discard(stack.pop())
        stack.append(c)
        cache.add(c)
      count[c] -= 1
    r_ "".join(stack)
