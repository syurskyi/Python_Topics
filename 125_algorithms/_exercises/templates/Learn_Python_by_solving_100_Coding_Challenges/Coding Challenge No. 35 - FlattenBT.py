# Flatten Binary Tree
# Question: Given a binary tree, flatten it to a linked list in-place.
# For example:
# Given
# 1
# / \
# 2 5
# / \ \
# 3 4 6
# The flattened tree should look like:
# 1 \ 2 \ 3 \ 4 \ 5 \ 6
# Solutions:


c_ TreeNode:
    ___  -(self, x):
        val _ x
        left _ N..
        right _ N..

c_ Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    ___ flatten(self, root):
        __ root __ N..:
            r_
        stack _ [root.right, root.left]
        current _ root
        while le.(stack) !_ 0:
            nextNode _ stack.p..()
            __ nextNode __ N..:
                continue
            ____
                current.left _ N..
                current.right _ nextNode
                current _ current.right
                stack.ap..(current.right)
                stack.ap..(current.left)

        r_ root

        ___ printtree(self, tree_node):
            __ tree_node.left is no. N..:
                printtree(tree_node.left)
            print(tree_node.val)
        __ tree_node.right is no. N..:
            printtree(tree_node.right)


__  -n __ '__main__':
    BT, BT.right, BT.right.right, BT.left, BT.left.right, BT.left.left _ TreeNode(1), TreeNode(5), TreeNode(6), TreeNode(2), TreeNode(4), TreeNode(3)
    LL _ Solution().flatten(BT)
    Solution().printtree(LL)