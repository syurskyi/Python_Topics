# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution o..
    ___ isBalanced  root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # Bottom-up recursion with sentinel -1
        __ root is N..:
            r_ True
        __ getDepth(root) < 0:
            r_ False
        r_ True
    
    ___ getDepth  node):
        __ node is N..:
            r_ 1
        ld = getDepth(node.left)
        __ ld < 0:
            r_ -1
        rd = getDepth(node.right)
        __ rd < 0:
            r_ -1
        ____ abs(ld - rd) > 1:
            r_ -1
        ____
            r_ max(ld, rd) + 1
    

    # https://discuss.leetcode.com/topic/7798/the-bottom-up-o-n-solution-would-be-better
    # def isBalanced(self, root):
    #     # Top-down recursion
    #     if root is None:
    #         return True
    #     left = self.depth(root.left)
    #     right = self.depth(root.right)
    #     return abs(left - right) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    # def depth(self, root):
    #     if root is None:
    #         return 0
    #     return max(self.depth(root.left), self.depth(root.right)) + 1
        



