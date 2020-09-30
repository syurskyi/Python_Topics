# Maximum Depth of Binary Tree
# Question: Given a binary tree, find its maximum depth.
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
# Solutions:


class TreeNode:
    ___ __init__(self, x):
        self.val _ x
        self.left _ N..
        self.right _ N..


class Solution:
    # @param root, a tree node
    # @return an integer
    ___ maxDepth_recursive(self, root):
        __ root __ N..:
            r_ 0
        r_ ma.(self.maxDepth(root.left),self.maxDepth(root.right))+1

    ___ maxDepth_interative(self, root):
        __ root __ N..:
            r_ 0
        nodeStack _ [root]
        depthStack _ [1]
        maxDepth _ 0
        while le.(nodeStack)>0:
            node _ nodeStack.p..()
            depth _ depthStack.p..()
            maxDepth _ maxDepth __ maxDepth > depth ____ depth
            __ node.left !_ N..:
                nodeStack.ap..(node.left)
                depthStack.ap..(depth+1)
            __ node.right !_ N..:
                nodeStack.ap..(node.right)
                depthStack.ap..(depth+1)
        r_ maxDepth


__  -n __ '__main__':
    BT, BT.right, BT.right.left _ TreeNode(1), TreeNode(2), TreeNode(3)
    print ( Solution().maxDepth_interative(BT) )