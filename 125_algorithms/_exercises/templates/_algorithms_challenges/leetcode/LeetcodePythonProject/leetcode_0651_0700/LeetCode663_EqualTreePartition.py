'''
Created on Oct 8, 2017

@author: MT
'''
# Definition for a binary tree node.
class TreeNode(object
    ___ __init__(self, x, left=None,right=None
        self.val = x
        self.left = left
        self.right = right

class Solution(object
    ___ checkEqualTree(self, root
        """
        :type root: TreeNode
        :rtype: bool
        """
        __ not root: r_ False
        r_ self.helper(root, 0, True)
    
    ___ helper(self, root, sumVal, firstLevel
        __ not root:
            r_ False
        __ sumVal __ self.sum(root) and not firstLevel:
            r_ True
        __ (root.left and self.helper(root.left, sumVal+root.val+self.sum(root.right), False)) or\
            (root.right and self.helper(root.right, sumVal+root.val+self.sum(root.left), False)):
            r_ True
        r_ False
    
    ___ sum(self, root
        __ not root: r_ 0
        res = root.val
        res += self.sum(root.left)
        res += self.sum(root.right)
        r_ res
    
    ___ sumVal(self, root
        __ not root: r_ 0
        r_ root.val +\
            self.sumVal(root.left)+\
            self.sumVal(root.right)
    
    ___ test(self
        testCases = [
            TreeNode(5, TreeNode(10), TreeNode(10, TreeNode(2), TreeNode(3))),
            TreeNode(1, TreeNode(2), TreeNode(10, TreeNode(2), TreeNode(20))),
            TreeNode(1, TreeNode(-1)),
            TreeNode(1, None, TreeNode(2)),
            TreeNode(2, TreeNode(1, TreeNode(0), TreeNode(2, TreeNode(3))), TreeNode(3)),
        ]
        for root in testCases:
            result = self.checkEqualTree(root)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
