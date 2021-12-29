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

class Solution:
    # @param root, a tree node
    # @return a tree node
    ___ recoverTree(self, root):
        self.prev = N..
        self.first = N..
        self.second = N..
        self.traverse(root)
        self.first.val, self.second.val = self.second.val, self.first.val
        r.. root

    ___ traverse(self, root):
        __ root __ n.. N..
            self.traverse(root.left)
            __ self.prev __ n.. N..
                __ self.first __ N.. a.. root.val < self.prev.val:
                    self.first = self.prev
                    self.second = root
                ____ self.first __ n.. N.. a.. root.val < self.prev.val:
                    self.second = root
            self.prev = root
            self.traverse(root.right)
