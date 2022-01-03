'''
Created on Mar 1, 2017

@author: MT
'''

# Definition for a binary tree node.
c_ TreeNode:
    ___ - , x, left=N.., right_ N..
        val = x
        left = left
        right = right

c_ Solution:
    # @param {TreeNode} root
    # @return {string[]}
    ___ binaryTreePaths(self, root):
        __ n.. root: r.. []
        res    # list
        helper(root, res, s..(root.val))
        r.. res
    
    ___ helper(self, root, res, curr):
        __ n.. root.left a.. n.. root.right:
            res.a..(curr)
            r..
        __ root.left:
            helper(root.left, res, curr+('->%s' % root.left.val))
        __ root.right:
            helper(root.right, res, curr+('->%s' % root.right.val))
    
    ___ test
        testCases = [
            TreeNode(1, TreeNode(2, N.., TreeNode(5)), TreeNode(3)),
        ]
        ___ root __ testCases:
            result = binaryTreePaths(root)
            print('result: %s' % (result))

__ __name__ __ '__main__':
    Solution().test()
