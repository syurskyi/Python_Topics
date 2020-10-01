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

c_ TreeNode:
    ___  -(, x):
        val _ x
        left _ N..
        right _ N..

c_ Solution:
    ___ inorderTraversal(root):
        stack _   # list
        node _ root
        solution _   # list
        w___ node!_ N.. o. le.(stack)>0:
            __ node !_ N..:
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