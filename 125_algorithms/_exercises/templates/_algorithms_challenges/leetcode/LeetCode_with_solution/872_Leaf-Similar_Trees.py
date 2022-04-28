# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution o..
    ___ leafSimilar  root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        __ not root1 and not root2:
            r_ True
        leaf1 = []
        leaf2 = []
        dfs(root1, leaf1)
        dfs(root2, leaf2)
        __ leaf1 __ leaf2:
            r_ True
        r_ False

    ___ dfs  node, leavels):
        __ not node:
            r_
        __ not node.left and not node.right:
            leavels.append(node.val)
        dfs(node.left, leavels)
        dfs(node.right, leavels)
