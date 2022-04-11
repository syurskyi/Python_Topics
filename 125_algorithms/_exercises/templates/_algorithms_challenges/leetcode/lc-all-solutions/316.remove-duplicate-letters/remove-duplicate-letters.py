c_ Solution(o..
  ___ removeDuplicateLetters  s
    """
    :type s: str
    :rtype: str
    """
    d    # dict
    count    # dict
    ___ c __ s:
      d[c] d.g.. c, 0) + 1
      count[c] count.g.. c, 0) + 1
    stack    # list
    cache s..()
    ___ c __ s:
      __ c n.. __ cache:
        w.... stack a.. stack[-1] > c a.. d[stack[-1]] > 1 a.. d[stack[-1]] != 1 a.. count[stack[-1]] > 0:
          cache.discard(stack.pop
        stack.a..(c)
        cache.add(c)
      count[c] -_ 1
    r.. "".j..(stack)
