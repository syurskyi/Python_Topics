"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes
in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor
is defined between two nodes v and w as the lowest node in T that has both v
and w as descendants (where we allow a node to be a descendant of itself).”

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4
For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3. Another
example is LCA of nodes 5 and 4 is 5, since a node can be a descendant of
itself according to the LCA definition.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    ___ lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # If both a and b exist in root, return their LCA;
        # if either a or b exist in root, return whichever exists;
        # if neither of them exist in root, return None
        __ root __ N..
            r.. N..
        ____ root __ p o. root __ q:
            r.. root
        ____:
            l = self.lowestCommonAncestor(root.left, p, q)
            r = self.lowestCommonAncestor(root.right, p, q)
            __ l __ n.. N.. a.. r __ n.. N..
                r.. root
            ____:
                __ l __ n.. N..
                    r.. l
                __ r __ n.. N..
                    r.. r
