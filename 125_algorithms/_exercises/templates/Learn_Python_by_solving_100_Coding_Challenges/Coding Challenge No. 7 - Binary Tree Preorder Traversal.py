# Return Binary Pre-order Traversal
# Question: Given a binary tree, return the preorder traversal of its nodes' values.
# For example:
# Given binary tree
# 1
# \
# 2
# /
# 3
# return [1,2,3].
# Solutions:

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(root):
        result = []
        stack = [root]

        while stack:
            node = stack.pop()
            if node:
                result.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return result

if __name__ == '__main__':
    BT, BT.right, BT.right.left = TreeNode(1), TreeNode(2), TreeNode(3)
    print ( Solution.preorderTraversal(BT) )