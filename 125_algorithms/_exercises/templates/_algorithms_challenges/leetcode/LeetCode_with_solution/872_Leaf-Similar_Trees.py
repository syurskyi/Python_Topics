# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution o..
    ___ leafSimilar  root1, root2
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        __ n.. root1 a.. n.. root2:
            r_ T..
        leaf1 =    # list
        leaf2 =    # list
        dfs(root1, leaf1)
        dfs(root2, leaf2)
        __ leaf1 __ leaf2:
            r_ T..
        r_ F..

    ___ dfs  node, leavels
        __ n.. node:
            r_
        __ n.. node.left a.. n.. node.right:
            leavels.append(node.val)
        dfs(node.left, leavels)
        dfs(node.right, leavels)
