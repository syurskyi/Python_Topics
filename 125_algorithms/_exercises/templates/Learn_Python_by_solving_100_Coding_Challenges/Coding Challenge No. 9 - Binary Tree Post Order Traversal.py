# Return Binary Post-order Traversal
# Question: Given a binary tree, return the postorder traversal of its nodes' values.
# For example:
# Given binary tree {1,2,3},
# 1
# \
# 2
# /
# 3
# return [3,2,1].
# Solutions:

class TreeNode:
    ___ __init__(self, x):
        self.val _ x
        self.left _ None
        self.right _ None

class Solution:
    ___ postorderTraversal(root):
        __ root __ None:
            r_   # list
        stackPrepare _ [root]
        stackReady _   # list
        result _   # list
        while le.(stackPrepare) !_ 0 :
            current _ stackPrepare.p..()
            stackReady.ap..(current)
            __ current.left !_ None: stackPrepare.ap..(current.left)
            __ current.right !_ None: stackPrepare.ap..(current.right)
        while le.(stackReady) !_ 0:
            result.ap..(stackReady.p..().val)
        r_ result

__  -n __ '__main__':
    BT, BT.right, BT.right.left _ TreeNode(1), TreeNode(2), TreeNode(3)
    print ( Solution. postorderTraversal (BT) )