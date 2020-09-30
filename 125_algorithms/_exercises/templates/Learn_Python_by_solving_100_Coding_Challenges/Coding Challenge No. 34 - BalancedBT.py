# Balanced Binary Tree
# Question: Given a binary tree, determine if it is height-balanced.
# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1
# Solutions:


c_ TreeNode:
    ___  -(self, x):
        val _ x
        left _ N..
        right _ N..


c_ Solution:
    # @param root, a tree node
    # @return a boolean
    ___ isBalanced(self, root):
        r_ isBalancedInt(root)>_0

    ___ isBalancedInt(self, root):
        __ root __ N..:
            r_ 0;
        left _ isBalancedInt(root.left)
        right _ isBalancedInt(root.right)
        __ left<0 or right<0 or abs(left-right)>1:
            r_ -1
        r_ ma.(left,right)+1

__  -n __ '__main__':
    BT, BT.right, BT.right.left _ TreeNode(1), TreeNode(2), TreeNode(3)
    print ( Solution().isBalanced(BT) )