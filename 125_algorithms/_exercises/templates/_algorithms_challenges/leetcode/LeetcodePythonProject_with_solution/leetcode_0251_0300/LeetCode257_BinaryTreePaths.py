'''
Created on Mar 1, 2017

@author: MT
'''

# Definition for a binary tree node.
class TreeNode:
    ___ __init__(self, x, left=N.., right_ N..
        self.val = x
        self.left = left
        self.right = right

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    ___ binaryTreePaths(self, root):
        __ n.. root: r.. []
        res    # list
        self.helper(root, res, s..(root.val))
        r.. res
    
    ___ helper(self, root, res, curr):
        __ n.. root.left a.. n.. root.right:
            res.a..(curr)
            r..
        __ root.left:
            self.helper(root.left, res, curr+('->%s' % root.left.val))
        __ root.right:
            self.helper(root.right, res, curr+('->%s' % root.right.val))
    
    ___ test(self):
        testCases = [
            TreeNode(1, TreeNode(2, N.., TreeNode(5)), TreeNode(3)),
        ]
        ___ root __ testCases:
            result = self.binaryTreePaths(root)
            print('result: %s' % (result))

__ __name__ __ '__main__':
    Solution().test()
