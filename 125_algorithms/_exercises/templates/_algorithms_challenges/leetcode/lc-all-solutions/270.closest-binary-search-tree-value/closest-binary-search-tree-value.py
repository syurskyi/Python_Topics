# Definition for a binary tree node.
# class TreeNode(object
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object
  ___ closestValue(self, p, target
    """
    :type root: TreeNode
    :type target: float
    :rtype: int
    """
    ans = p.val
    w___ p:
      __ abs(target - p.val) < abs(ans - target
        ans = p.val
      __ target < p.val:
        p = p.left
      ____
        p = p.right
    r_ ans
