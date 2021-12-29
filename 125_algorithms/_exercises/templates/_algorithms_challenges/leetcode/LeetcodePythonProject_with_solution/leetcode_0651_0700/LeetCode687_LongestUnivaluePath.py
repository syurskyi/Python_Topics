'''
Created on Oct 22, 2017

@author: MT
'''
# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x, left=N.., right_ N..
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    ___ longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxLen = 0
        self.helper(root)
        r.. self.maxLen
    
    ___ helper(self, root):
        __ n.. root: r.. 0
        left = self.helper(root.left)
        right = self.helper(root.right)
        __ root.left a.. root.left.val __ root.val:
            left += 1
        ____:
            left = 0
        __ root.right a.. root.right.val __ root.val:
            right += 1
        ____:
            right = 0
        self.maxLen = max(self.maxLen, left+right)
        r.. max(left, right)
    
    ___ test(self):
        testCases = [
            TreeNode(5, TreeNode(4, TreeNode(1), TreeNode(1)), TreeNode(5, N.., TreeNode(5))),
            TreeNode(1, TreeNode(4, TreeNode(4), TreeNode(4)), TreeNode(5, N.., TreeNode(5))),
        ]
        ___ root __ testCases:
            result = self.longestUnivaluePath(root)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
