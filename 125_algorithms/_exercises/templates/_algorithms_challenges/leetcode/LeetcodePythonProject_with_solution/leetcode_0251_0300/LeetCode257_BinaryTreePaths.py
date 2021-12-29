'''
Created on Mar 1, 2017

@author: MT
'''

# Definition for a binary tree node.
class TreeNode:
    ___ __init__(self, x, left=None, right_ N..
        self.val = x
        self.left = left
        self.right = right

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    ___ binaryTreePaths(self, root):
        __ not root: return []
        res = []
        self.helper(root, res, str(root.val))
        return res
    
    ___ helper(self, root, res, curr):
        __ not root.left and not root.right:
            res.append(curr)
            return
        __ root.left:
            self.helper(root.left, res, curr+('->%s' % root.left.val))
        __ root.right:
            self.helper(root.right, res, curr+('->%s' % root.right.val))
    
    ___ test(self):
        testCases = [
            TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3)),
        ]
        for root in testCases:
            result = self.binaryTreePaths(root)
            print('result: %s' % (result))

__ __name__ == '__main__':
    Solution().test()
