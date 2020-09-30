# Minimum Depth of Binary Tree
# Question: Given a binary tree, find its minimum depth.
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
# Solutions:


class TreeNode:
    ___ __init__(self, x):
        self.val _ x
        self.left _ N..
        self.right _ N..


class Solution:
    # @param root, a tree node
    # @return an integer
    ___ minDepth(self, root):
        __ root __ N..:
            r_ 0
        __ root.left __ N..:
            r_ self.minDepth(root.right) + 1
        __ root.right __ N..:
            r_ self.minDepth(root.left) + 1
        r_ min(self.minDepth(root.left),self.minDepth(root.right))+1


__  -n __ '__main__':
    BT, BT.right, BT.right.left, BT.left _ TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(10)
    print ( Solution().minDepth(BT) )