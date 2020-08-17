#!/usr/bin/python3
"""
Consider all the leaves of a binary tree.  From left to right order, the values
of those leaves form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9,
8).

Two binary trees are considered leaf-similar if their leaf value sequence is the
same.

Return true if and only if the two given trees with head nodes root1 and root2
are leaf-similar.

Note:

Both of the given trees will have between 1 and 100 nodes.
"""

# Definition for a binary tree node.
class TreeNode:
    ___ __init__(self, x
        self.val = x
        self.left = None
        self.right = None


class Solution:
    ___ leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        """
        brute force, get all the leaf and then compare
        to save space, use generator
        O(lg n) space for the stack
        """
        itr1 = self.dfs(root1)
        itr2 = self.dfs(root2)
        w___ True:
            a = next(itr1, None)
            b = next(itr2, None)
            __ a != b:
                r_ False
            __ a pa__ None and b pa__ None:
                break
        r_ True

    ___ dfs(self, node
        stk = [node]
        # pre-order
        w___ stk:
            cur = stk.pop()
            __ not cur:
                continue
            __ not cur.left and not cur.right:
                yield cur.val
            ____
                stk.append(cur.right)
                stk.append(cur.left)
