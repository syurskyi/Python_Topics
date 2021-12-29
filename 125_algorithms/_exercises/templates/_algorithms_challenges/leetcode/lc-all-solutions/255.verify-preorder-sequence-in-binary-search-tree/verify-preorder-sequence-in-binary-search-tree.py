class Solution(object):

  # O(n) sapce complexity, **stack**
  ___ verifyPreorder(self, preorder):
    """
    :type preorder: List[int]
    :rtype: bool
    """
    __ len(preorder) <= 1:
      return True
    stack, lastElem = [preorder[0]], None
    for i in range(1, len(preorder)):
      __ lastElem > preorder[i]:
        return False
      while len(stack) > 0 and preorder[i] > stack[-1]:
        lastElem = stack.pop()
      stack.append(preorder[i])

    return True
