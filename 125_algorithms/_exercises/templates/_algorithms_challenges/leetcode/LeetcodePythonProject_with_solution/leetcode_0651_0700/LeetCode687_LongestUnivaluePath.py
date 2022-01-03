'''
Created on Oct 22, 2017

@author: MT
'''
# Definition for a binary tree node.
c_ TreeNode(object):
    ___ - , x, left=N.., right_ N..
        val = x
        left = left
        right = right

c_ Solution(object):
    ___ longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        maxLen = 0
        helper(root)
        r.. maxLen
    
    ___ helper(self, root):
        __ n.. root: r.. 0
        left = helper(root.left)
        right = helper(root.right)
        __ root.left a.. root.left.val __ root.val:
            left += 1
        ____:
            left = 0
        __ root.right a.. root.right.val __ root.val:
            right += 1
        ____:
            right = 0
        maxLen = max(maxLen, left+right)
        r.. max(left, right)
    
    ___ test
        testCases = [
            TreeNode(5, TreeNode(4, TreeNode(1), TreeNode(1)), TreeNode(5, N.., TreeNode(5))),
            TreeNode(1, TreeNode(4, TreeNode(4), TreeNode(4)), TreeNode(5, N.., TreeNode(5))),
        ]
        ___ root __ testCases:
            result = longestUnivaluePath(root)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
