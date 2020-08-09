# Definition for a binary tree node.
# class TreeNode(object
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object
  ___ boundaryOfBinaryTree(self, root
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    __ not root:
      r_ []

    ___ dfsLeft(root, res
      __ not root or (not root.left and not root.right
        r_
      res.append(root.val)
      __ root.left:
        dfsLeft(root.left, res)
      ____
        dfsLeft(root.right, res)

    ___ dfsRight(root, res
      __ not root or (not root.left and not root.right
        r_
      __ root.right:
        dfsRight(root.right, res)
      ____
        dfsRight(root.left, res)
      res.append(root.val)

    ___ dfsLeaves(root, res, mid
      __ not root:
        r_
      __ not root.left and not root.right and root != mid:
        res.append(root.val)
      dfsLeaves(root.left, res, mid)
      dfsLeaves(root.right, res, mid)

    res = [root.val]
    dfsLeft(root.left, res)
    dfsLeaves(root, res, root)
    dfsRight(root.right, res)
    r_ res
