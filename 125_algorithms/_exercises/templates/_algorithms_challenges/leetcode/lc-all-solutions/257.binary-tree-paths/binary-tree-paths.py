# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution:
  # @param {TreeNode} root
  # @return {string[]}
  ___ binaryTreePaths  root
    ___ helper(root, p.., res
      __ root:
        p...a..(s..(root.val
        left helper(root.left, p.., res)
        right helper(root.right, p.., res)
        __ n.. left a.. n.. right:
          res.a..("->".j..(p..
        p...p.. )
        r.. T..

    res    # list
    helper(root, [], res)
    r.. res
