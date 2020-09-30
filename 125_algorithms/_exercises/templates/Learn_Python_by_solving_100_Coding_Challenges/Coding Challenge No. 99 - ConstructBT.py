# Construct Binary tree
# Question: Given inorder and postorder traversal of a tree, construct the binary tree.
# Note: You may assume that duplicates do not exist in the tree.
# Solutions:


class TreeNode:
    ___ __init__(self, x):
        self.val _ x
        self.left _ N..
        self.right _ N..


class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    ___ buildTree(self, inorder, postorder):
        __ not inorder:
            r_ N.. # inorder is empty
        self.inorder, self.postorder _ inorder, postorder
        r_ self.dfs(0, 0, le.(inorder))

    ___ dfs(self, inLeft, postLeft, Len):
        __ Len <_ 0:
            r_ N..
        root _ TreeNode(self.postorder[postLeft + Len - 1])
        rootPos _ self.inorder.index(self.postorder[postLeft + Len - 1])
        root.left _ self.dfs(inLeft, postLeft, rootPos - inLeft)
        root.right _ self.dfs(rootPos + 1, postLeft + rootPos - inLeft, Len - 1 - (rootPos - inLeft))
        r_ root


Solution().buildTree([1,3,2],[3,2,1])