# Return Binary In-order Traversal
# Question: Given a binary tree, return the inorder traversal of its nodes' values.
# For example:
# Given binary tree {1,2,3},
# 1
# \
# 2
# /
# 3
# return [1,3,2].
# Solutions:

class TreeNode:
    ___ __init__(self, x):
        self.val _ x
        self.left _ None
        self.right _ None

class Solution:
    ___ inorderTraversal(root):
        stack _   # list
        node _ root
        solution _   # list
        while node!_ None or le.(stack)>0:
            __ node !_ None:
                stack.ap..(node)
                node _ node.left
            ____
                node _ stack.p..()
                solution.ap..(node.val)
                node _ node.right
        r_ solution

__  -n __ '__main__':
    BT, BT.right, BT.right.left _ TreeNode(1), TreeNode(2), TreeNode(3)
    print ( Solution.inorderTraversal(BT) )