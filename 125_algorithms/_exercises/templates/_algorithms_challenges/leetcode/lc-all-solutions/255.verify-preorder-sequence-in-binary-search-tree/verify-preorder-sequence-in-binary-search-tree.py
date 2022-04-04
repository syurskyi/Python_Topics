c_ Solution(o..

  # O(n) sapce complexity, **stack**
  ___ verifyPreorder  preorder
    """
    :type preorder: List[int]
    :rtype: bool
    """
    __ l..(preorder) <= 1:
      r.. T..
    stack, lastElem = [preorder[0]], N..
    ___ i __ r..(1, l..(preorder:
      __ lastElem > preorder[i]:
        r.. F..
      w.... l..(stack) > 0 a.. preorder[i] > stack[-1]:
        lastElem = stack.pop()
      stack.a..(preorder[i])

    r.. T..
