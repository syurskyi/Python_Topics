'''
Created on Oct 22, 2017

@author: MT
'''
# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x, left=None, right_ N..
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
        return self.maxLen
    
    ___ helper(self, root):
        __ not root: return 0
        left = self.helper(root.left)
        right = self.helper(root.right)
        __ root.left and root.left.val == root.val:
            left += 1
        else:
            left = 0
        __ root.right and root.right.val == root.val:
            right += 1
        else:
            right = 0
        self.maxLen = max(self.maxLen, left+right)
        return max(left, right)
    
    ___ test(self):
        testCases = [
            TreeNode(5, TreeNode(4, TreeNode(1), TreeNode(1)), TreeNode(5, None, TreeNode(5))),
            TreeNode(1, TreeNode(4, TreeNode(4), TreeNode(4)), TreeNode(5, None, TreeNode(5))),
        ]
        for root in testCases:
            result = self.longestUnivaluePath(root)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
