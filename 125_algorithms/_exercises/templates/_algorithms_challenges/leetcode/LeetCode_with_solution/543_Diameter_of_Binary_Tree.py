# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution o..
    # https://leetcode.com/problems/diameter-of-binary-tree/solution/
    ___ diameterOfBinaryTree  root
        ans = 1
        ___ depth(node
            __ n.. node: r_ 0
            L = depth(node.left)
            R = depth(node.right)
            ans = m..(ans, L+R+1)
            r_ m..(L, R) + 1

        depth(root)
        # number of nodes - 1 = length
        r_ ans - 1
