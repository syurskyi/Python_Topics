# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution(o..
  ___ closestKValues  root, target, k
    """
    :type root: TreeNode
    :type target: float
    :type k: int
    :rtype: List[int]
    """
    ans    # list
    preStack    # list
    sucStack    # list

    w.... root:
      __ root.val < target:
        preStack.a..(root)
        root = root.right
      ____
        sucStack.a..(root)
        root = root.left

    ___ getPredecessor(stack
      __ n.. stack:
        r..
      pre = stack.p.. )
      p = pre.left
      w.... p:
        stack.a..(p)
        p = p.right
      r.. pre

    ___ getSuccessor(stack
      __ n.. stack:
        r..
      suc = stack.p.. )
      p = suc.right
      w.... p:
        stack.a..(p)
        p = p.left
      r.. suc

    pre = getPredecessor(preStack)
    suc = getSuccessor(sucStack)

    w.... k:
      k -= 1
      __ pre a.. n.. suc:
        ans.a..(pre.val)
        pre = getPredecessor(preStack)
      ____ n.. pre a.. suc:
        ans.a..(suc.val)
        suc = getSuccessor(sucStack)
      ____ pre a.. suc a.. a..(pre.val - target) <_ a..(suc.val - target
        ans.a..(pre.val)
        pre = getPredecessor(preStack)
      ____ pre a.. suc a.. a..(pre.val - target) >_ a..(suc.val - target
        ans.a..(suc.val)
        suc = getSuccessor(sucStack)
    r.. ans
