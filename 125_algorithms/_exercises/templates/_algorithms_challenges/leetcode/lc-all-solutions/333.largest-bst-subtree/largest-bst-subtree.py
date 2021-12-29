# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  ___ largestBSTSubtree(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """

    ___ helper(root):
      __ n.. root:
        r.. (0, 0, float("inf"), float("-inf"))  # numBST, maxNumBST, min, max
      lnumBST, lmaxNumBST, lmin, lmax = helper(root.left)
      rnumBST, rmaxNumBST, rmin, rmax = helper(root.right)
      numBST = -1
      __ lmax < root.val < rmin a.. lnumBST != -1 a.. rnumBST != -1:
        numBST = 1 + lnumBST + rnumBST
      maxNumBST = max(1, lmaxNumBST, rmaxNumBST, numBST)
      r.. numBST, maxNumBST, m..(lmin, rmin, root.val), max(lmax, rmax, root.val)

    r.. helper(root)[1]
