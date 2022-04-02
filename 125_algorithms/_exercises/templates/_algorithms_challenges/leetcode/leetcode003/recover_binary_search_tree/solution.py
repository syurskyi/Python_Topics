"""
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Note:
A solution using O(n) space is pretty straight forward. Could you devise a
constant space solution?
"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution:
    # @param root, a tree node
    # @return a tree node
    ___ recoverTree  root
        prev = N..
        first = N..
        second = N..
        traverse(root)
        first.val, second.val = second.val, first.val
        r.. root

    ___ traverse  root
        __ root __ n.. N..
            traverse(root.left)
            __ prev __ n.. N..
                __ first __ N.. a.. root.val < prev.val:
                    first = prev
                    second = root
                ____ first __ n.. N.. a.. root.val < prev.val:
                    second = root
            prev = root
            traverse(root.right)
