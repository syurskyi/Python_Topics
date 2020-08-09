# Definition for a binary tree node.
# class TreeNode(object
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object
  ___ closestKValues(self, root, target, k
    """
    :type root: TreeNode
    :type target: float
    :type k: int
    :rtype: List[int]
    """
    ans = []
    preStack = []
    sucStack = []

    w___ root:
      __ root.val < target:
        preStack.append(root)
        root = root.right
      ____
        sucStack.append(root)
        root = root.left

    ___ getPredecessor(stack
      __ not stack:
        r_
      pre = stack.pop()
      p = pre.left
      w___ p:
        stack.append(p)
        p = p.right
      r_ pre

    ___ getSuccessor(stack
      __ not stack:
        r_
      suc = stack.pop()
      p = suc.right
      w___ p:
        stack.append(p)
        p = p.left
      r_ suc

    pre = getPredecessor(preStack)
    suc = getSuccessor(sucStack)

    w___ k:
      k -= 1
      __ pre and not suc:
        ans.append(pre.val)
        pre = getPredecessor(preStack)
      ____ not pre and suc:
        ans.append(suc.val)
        suc = getSuccessor(sucStack)
      ____ pre and suc and abs(pre.val - target) <= abs(suc.val - target
        ans.append(pre.val)
        pre = getPredecessor(preStack)
      ____ pre and suc and abs(pre.val - target) >= abs(suc.val - target
        ans.append(suc.val)
        suc = getSuccessor(sucStack)
    r_ ans
