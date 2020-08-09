# -*- coding: utf-8 -*-
"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the
lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4
For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3. Another example is LCA of nodes 5 and 4 is 5, since
a node can be a descendant of itself according to the LCA definition.
"""
__author__ = 'Daniel'


class TreeNode:
    ___ __init__(self, x
        self.val = x
        self.left = None
        self.right = None


class Solution:
    ___ lowestCommonAncestor(self, root, p, q
        """
        O(n)
        construct the path from root to p and q respectively, and check the difference of the two paths

        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        path1, path2 = [], []
        self.dfs(root, p, path1, [False])
        self.dfs(root, q, path2, [False])

        i = 0
        w___ i < min(le.(path1), le.(path2)):
            __ path1[i] != path2[i]:
                r_ path1[i-1]
            i += 1

        r_ path1[i-1]

    ___ dfs(self, root, t, path, found
        __ not root or found[0]:  # post-call check
            r_

        path.append(root)
        __ root __ t:
            found[0] = True

        self.dfs(root.left, t, path, found)
        self.dfs(root.right, t, path, found)
        __ not found[0]:
            path.pop()  # 1 pop() corresponds to 1 append()

