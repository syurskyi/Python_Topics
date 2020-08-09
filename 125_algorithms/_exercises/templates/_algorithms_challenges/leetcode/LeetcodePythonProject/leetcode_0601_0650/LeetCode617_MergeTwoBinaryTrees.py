'''
Created on Sep 7, 2017

@author: MT
'''
# Definition for a binary tree node.
class TreeNode(object
    ___ __init__(self, x, left=None, right=None
        self.val = x
        self.left = left
        self.right = right

class Solution(object
    ___ mergeTrees(self, t1, t2
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        root = TreeNode(-1)
        __ t1 and not t2:
            root.val = t1.val
            root.left = self.mergeTrees(t1.left, t2)
            root.right = self.mergeTrees(t1.right, t2)
        ____ not t1 and t2:
            root.val = t2.val
            root.left = self.mergeTrees(t1, t2.left)
            root.right = self.mergeTrees(t1, t2.right)
        ____ t1 and t2:
            root.val = t1.val + t2.val
            root.left = self.mergeTrees(t1.left, t2.left)
            root.right = self.mergeTrees(t1.right, t2.right)
        ____
            root = None
        r_ root
    
    ___ test(self
        testCases = [
            [
                TreeNode(1, TreeNode(3, TreeNode(5)), TreeNode(2)),
                TreeNode(2, TreeNode(1, None, TreeNode(4)), TreeNode(3, None, TreeNode(7))),
            ],
        ]
        for t1, t2 in testCases:
            root = self.mergeTrees(t1, t2)
            print(root.val)

__ __name__ __ '__main__':
    Solution().test()
