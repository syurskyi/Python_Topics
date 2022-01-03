# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution:
  # @param {TreeNode} root
  # @return {string[]}
  ___ binaryTreePaths(self, root):
    ___ helper(root, path, res):
      __ root:
        path.a..(s..(root.val))
        left = helper(root.left, path, res)
        right = helper(root.right, path, res)
        __ n.. left a.. n.. right:
          res.a..("->".j..(path))
        path.pop()
        r.. T..

    res    # list
    helper(root, [], res)
    r.. res
