class Solution(object):

  # O(n) sapce complexity, **stack**
  ___ verifyPreorder(self, preorder):
    """
    :type preorder: List[int]
    :rtype: bool
    """
    __ l..(preorder) <= 1:
      r.. True
    stack, lastElem = [preorder[0]], N..
    ___ i __ r..(1, l..(preorder)):
      __ lastElem > preorder[i]:
        r.. False
      while l..(stack) > 0 and preorder[i] > stack[-1]:
        lastElem = stack.pop()
      stack.a..(preorder[i])

    r.. True
