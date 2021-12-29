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
    ans    # list
    preStack    # list
    sucStack    # list

    while root:
      __ root.val < target:
        preStack.a..(root)
        root = root.right
      ____:
        sucStack.a..(root)
        root = root.left

    ___ getPredecessor(stack):
      __ n.. stack:
        r..
      pre = stack.pop()
      p = pre.left
      while p:
        stack.a..(p)
        p = p.right
      r.. pre

    ___ getSuccessor(stack):
      __ n.. stack:
        r..
      suc = stack.pop()
      p = suc.right
      while p:
        stack.a..(p)
        p = p.left
      r.. suc

    pre = getPredecessor(preStack)
    suc = getSuccessor(sucStack)

    while k:
      k -= 1
      __ pre and n.. suc:
        ans.a..(pre.val)
        pre = getPredecessor(preStack)
      ____ n.. pre and suc:
        ans.a..(suc.val)
        suc = getSuccessor(sucStack)
      ____ pre and suc and abs(pre.val - target) <= abs(suc.val - target):
        ans.a..(pre.val)
        pre = getPredecessor(preStack)
      ____ pre and suc and abs(pre.val - target) >= abs(suc.val - target):
        ans.a..(suc.val)
        suc = getSuccessor(sucStack)
    r.. ans
