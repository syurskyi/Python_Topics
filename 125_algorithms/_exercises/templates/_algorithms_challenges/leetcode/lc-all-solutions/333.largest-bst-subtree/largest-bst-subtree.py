# Definition for a binary tree node.
# class TreeNode(object
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object
  ___ largestBSTSubtree(self, root
    """
    :type root: TreeNode
    :rtype: int
    """

    ___ helper(root
      __ not root:
        r_ (0, 0, float("inf"), float("-inf"))  # numBST, maxNumBST, min, max
      lnumBST, lmaxNumBST, lmin, lmax = helper(root.left)
      rnumBST, rmaxNumBST, rmin, rmax = helper(root.right)
      numBST = -1
      __ lmax < root.val < rmin and lnumBST != -1 and rnumBST != -1:
        numBST = 1 + lnumBST + rnumBST
      maxNumBST = ma.(1, lmaxNumBST, rmaxNumBST, numBST)
      r_ numBST, maxNumBST, min(lmin, rmin, root.val), ma.(lmax, rmax, root.val)

    r_ helper(root)[1]
