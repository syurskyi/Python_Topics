# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution(o..
  ___ closestValue  p, target
    """
    :type root: TreeNode
    :type target: float
    :rtype: int
    """
    ans = p.val
    w.... p:
      __ a..(target - p.val) < a..(ans - target
        ans = p.val
      __ target < p.val:
        p = p.left
      ____
        p = p.right
    r.. ans
