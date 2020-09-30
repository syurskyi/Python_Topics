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
        self.val = x
        self.left = None
        self.right = None

class Solution:
    ___ postorderTraversal(root):
        if root == None:
            r_   # list
        stackPrepare = [root]
        stackReady =   # list
        result =   # list
        while len(stackPrepare) != 0 :
            current = stackPrepare.pop()
            stackReady.append(current)
            if current.left != None: stackPrepare.append(current.left)
            if current.right != None: stackPrepare.append(current.right)
        while len(stackReady) != 0:
            result.append(stackReady.pop().val)
        r_ result

if  -n == '__main__':
    BT, BT.right, BT.right.left = TreeNode(1), TreeNode(2), TreeNode(3)
    print ( Solution. postorderTraversal (BT) )