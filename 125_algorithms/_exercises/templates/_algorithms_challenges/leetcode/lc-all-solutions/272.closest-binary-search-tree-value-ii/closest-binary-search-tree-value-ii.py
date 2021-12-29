# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  ___ closestKValues(self, root, target, k):
    """
    :type root: TreeNode
    :type target: float
    :type k: int
    :rtype: List[int]
    """
    ans = []
    preStack = []
    sucStack = []

    while root:
      __ root.val < target:
        preStack.append(root)
        root = root.right
      else:
        sucStack.append(root)
        root = root.left

    ___ getPredecessor(stack):
      __ not stack:
        return
      pre = stack.pop()
      p = pre.left
      while p:
        stack.append(p)
        p = p.right
      return pre

    ___ getSuccessor(stack):
      __ not stack:
        return
      suc = stack.pop()
      p = suc.right
      while p:
        stack.append(p)
        p = p.left
      return suc

    pre = getPredecessor(preStack)
    suc = getSuccessor(sucStack)

    while k:
      k -= 1
      __ pre and not suc:
        ans.append(pre.val)
        pre = getPredecessor(preStack)
      elif not pre and suc:
        ans.append(suc.val)
        suc = getSuccessor(sucStack)
      elif pre and suc and abs(pre.val - target) <= abs(suc.val - target):
        ans.append(pre.val)
        pre = getPredecessor(preStack)
      elif pre and suc and abs(pre.val - target) >= abs(suc.val - target):
        ans.append(suc.val)
        suc = getSuccessor(sucStack)
    return ans
