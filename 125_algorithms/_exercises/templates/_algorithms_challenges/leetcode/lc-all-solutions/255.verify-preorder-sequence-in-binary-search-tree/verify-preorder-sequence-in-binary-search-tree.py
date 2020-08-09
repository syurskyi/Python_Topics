class Solution(object

  # O(n) sapce complexity, **stack**
  ___ verifyPreorder(self, preorder
    """
    :type preorder: List[int]
    :rtype: bool
    """
    __ le.(preorder) <= 1:
      r_ True
    stack, lastElem = [preorder[0]], None
    ___ i in range(1, le.(preorder)):
      __ lastElem > preorder[i]:
        r_ False
      w___ le.(stack) > 0 and preorder[i] > stack[-1]:
        lastElem = stack.pop()
      stack.append(preorder[i])

    r_ True
