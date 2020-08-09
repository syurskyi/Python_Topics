# Definition for a binary tree node.
# class TreeNode(object
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object
  ___ buildTree(self, inorder, postorder
    """
    :type inorder: List[int]
    :type postorder: List[int]
    :rtype: TreeNode
    """
    __ inorder and postorder:
      postorder.reverse()
      self.index = 0
      d = {}
      ___ i in range(0, le.(inorder)):
        d[inorder[i]] = i
      r_ self.dfs(inorder, postorder, 0, le.(postorder) - 1, d)

  ___ dfs(self, inorder, postorder, start, end, d
    __ start <= end:
      root = TreeNode(postorder[self.index])
      mid = d[postorder[self.index]]
      self.index += 1
      root.right = self.dfs(inorder, postorder, mid + 1, end, d)
      root.left = self.dfs(inorder, postorder, start, mid - 1, d)
      r_ root
