# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
  # @param {TreeNode} root
  # @return {string[]}
  ___ binaryTreePaths(self, root):
    ___ helper(root, path, res):
      __ root:
        path.a..(str(root.val))
        left = helper(root.left, path, res)
        right = helper(root.right, path, res)
        __ n.. left and n.. right:
          res.a..("->".join(path))
        path.pop()
        r.. True

    res    # list
    helper(root, [], res)
    r.. res
