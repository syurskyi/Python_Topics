'''
Created on Feb 9, 2017

@author: MT
'''
# Definition for a binary tree node.
class TreeNode(object
    ___ __init__(self, x, left=None, right=None
        self.val = x
        self.left = left
        self.right = right

class Solution(object
    ___ preorderTraversal(self, root
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        __ not root: r_ []
        stack = [root]
        res = []
        w___ stack:
            node = stack.pop()
            res.append(node.val)
            __ node.right:
                stack.append(node.right)
            __ node.left:
                stack.append(node.left)
        r_ res
    
    ___ test(self
        testCases = [
            TreeNode(5, TreeNode(3, TreeNode(1), TreeNode(4)), TreeNode(7, None, TreeNode(9)))
        ]
        for root in testCases:
            result = self.preorderTraversal(root)
            print('result: %s' % (result))

__ __name__ __ '__main__':
    Solution().test()