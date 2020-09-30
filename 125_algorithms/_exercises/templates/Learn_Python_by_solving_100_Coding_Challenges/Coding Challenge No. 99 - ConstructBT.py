# Construct Binary tree
# Question: Given inorder and postorder traversal of a tree, construct the binary tree.
# Note: You may assume that duplicates do not exist in the tree.
# Solutions:


c_ TreeNode:
    ___  -(self, x):
        val _ x
        left _ N..
        right _ N..


c_ Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    ___ buildTree(self, inorder, postorder):
        __ not inorder:
            r_ N.. # inorder is empty
        inorder, postorder _ inorder, postorder
        r_ dfs(0, 0, le.(inorder))

    ___ dfs(self, inLeft, postLeft, Len):
        __ Len <_ 0:
            r_ N..
        root _ TreeNode(postorder[postLeft + Len - 1])
        rootPos _ inorder.index(postorder[postLeft + Len - 1])
        root.left _ dfs(inLeft, postLeft, rootPos - inLeft)
        root.right _ dfs(rootPos + 1, postLeft + rootPos - inLeft, Len - 1 - (rootPos - inLeft))
        r_ root


Solution().buildTree([1,3,2],[3,2,1])