"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two
given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor
is defined between two nodes v and w as the lowest node in T that has both v
and w as descendants (where we allow a node to be a descendant of itself).”

        _______6______
       /              \
    ___2__          ___8__
   /      \        /      \
   0      _4       7       9
         /  \
         3   5
For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6. Another
example is LCA of nodes 2 and 4 is 2, since a node can be a descendant of
itself according to the LCA definition.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution(o..
    ___ lowestCommonAncestor  root, p, q
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        __ root __ N..
            r.. N..
        ____
            __ m..(p.val, q.val) <= root.val <= m..(p.val, q.val
                r.. root
            ____ root.val > m..(p.val, q.val
                r.. lowestCommonAncestor(root.left, p, q)
            ____
                r.. lowestCommonAncestor(root.right, p, q)
