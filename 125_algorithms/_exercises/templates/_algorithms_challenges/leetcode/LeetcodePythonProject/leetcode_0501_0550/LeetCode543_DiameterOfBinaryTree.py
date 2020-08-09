'''
Created on Aug 20, 2017

@author: MT
'''

# Definition for a binary tree node.
class TreeNode(object
    ___ __init__(self, x, left=None, right=None
        self.val = x
        self.left = left
        self.right = right

class Solution(object
    ___ diameterOfBinaryTree(self, root
        """
        :type root: TreeNode
        :rtype: int
        """
        __ not root: r_ 0
        r_ self.helper(root)[-1]-1
    
    # returns include, exclude
    ___ helper(self, root
        __ not root:
            r_ 0, 0
        left = self.helper(root.left)
        right = self.helper(root.right)
        include = max(1+left[0], 1+right[0])
        exclude = max([left[1], right[1], left[0]+right[0]+1])
        r_ include, exclude
    
    ___ test(self
        testCases = [
            TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3)),
        ]
        for root in testCases:
            result = self.diameterOfBinaryTree(root)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
