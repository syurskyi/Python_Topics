'''
Created on Feb 9, 2017

@author: MT
'''
# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x, left=N.., right_ N..
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    ___ preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        __ n.. root: r.. []
        stack = [root]
        res    # list
        while stack:
            node = stack.pop()
            res.a..(node.val)
            __ node.right:
                stack.a..(node.right)
            __ node.left:
                stack.a..(node.left)
        r.. res
    
    ___ test(self):
        testCases = [
            TreeNode(5, TreeNode(3, TreeNode(1), TreeNode(4)), TreeNode(7, N.., TreeNode(9)))
        ]
        ___ root __ testCases:
            result = self.preorderTraversal(root)
            print('result: %s' % (result))

__ __name__ __ '__main__':
    Solution().test()