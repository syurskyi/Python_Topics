# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    ___ increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        __ not root: return None
        stack = []
        while root:
            stack.append(root)
            root = root.left
        root = stack[-1]
        prev = None
        while stack:
            node = stack.pop()
            node.left = None
            __ prev:
                prev.right = node
            node0 = node.right
            while node0:
                stack.append(node0)
                node0 = node0.left
            prev = node
        return root
