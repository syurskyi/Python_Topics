"""
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    ___ binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res    # list
        cand    # list
        self.binary_tree_paths(root, cand, res)
        r.. res

    ___ binary_tree_paths(self, root, cand, res):
        __ root __ N..
            r..
        ____:
            cand.a..(root.val)
            __ root.left __ N.. and root.right __ N..
                p = '->'.join(map(str, cand))
                res.a..(p)
            self.binary_tree_paths(root.left, cand, res)
            self.binary_tree_paths(root.right, cand, res)
            cand.pop()
