# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x):
        self.val = x
        self.left = N..
        self.right = N..

class Solution(object):
    ___ increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        __ n.. root: r.. N..
        stack    # list
        while root:
            stack.a..(root)
            root = root.left
        root = stack[-1]
        prev = N..
        while stack:
            node = stack.pop()
            node.left = N..
            __ prev:
                prev.right = node
            node0 = node.right
            while node0:
                stack.a..(node0)
                node0 = node0.left
            prev = node
        r.. root
