'''
Created on Aug 29, 2017

@author: MT
'''
# Definition for a binary tree node.
class TreeNode(object
    ___ __init__(self, x, left=None, right=None
        self.val = x
        self.left = left
        self.right = right

class Solution(object
    ___ findTilt(self, root
        """
        :type root: TreeNode
        :rtype: int
        """
        res = [0]
        self.helper(root, res)
        r_ res[0]
    
    ___ helper(self, root, res
        __ not root: r_
        self.helper(root.left, res)
        self.helper(root.right, res)
        leftSum = self.getSum(root.left)
        rightSum = self.getSum(root.right)
        res[0] += abs(leftSum-rightSum)
    
    ___ getSum(self, root
        __ not root: r_ 0
        res = root.val
        res += self.getSum(root.left)
        res += self.getSum(root.right)
        r_ res
    
    ___ test(self
        testCases = [
            TreeNode(1, TreeNode(2), TreeNode(3)),
            TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, TreeNode(5))),
        ]
        ___ root in testCases:
            result = self.findTilt(root)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
