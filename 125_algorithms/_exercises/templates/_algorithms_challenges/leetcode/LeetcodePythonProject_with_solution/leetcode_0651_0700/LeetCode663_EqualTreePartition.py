'''
Created on Oct 8, 2017

@author: MT
'''
# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x, left=N..,right_ N..
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    ___ checkEqualTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        __ n.. root: r.. False
        r.. self.helper(root, 0, True)
    
    ___ helper(self, root, sumVal, firstLevel):
        __ n.. root:
            r.. False
        __ sumVal __ self.s..(root) a.. n.. firstLevel:
            r.. True
        __ (root.left a.. self.helper(root.left, sumVal+root.val+self.s..(root.right), False)) o.\
            (root.right a.. self.helper(root.right, sumVal+root.val+self.s..(root.left), False)):
            r.. True
        r.. False
    
    ___ s..(self, root):
        __ n.. root: r.. 0
        res = root.val
        res += self.s..(root.left)
        res += self.s..(root.right)
        r.. res
    
    ___ sumVal(self, root):
        __ n.. root: r.. 0
        r.. root.val +\
            self.sumVal(root.left)+\
            self.sumVal(root.right)
    
    ___ test(self):
        testCases = [
            TreeNode(5, TreeNode(10), TreeNode(10, TreeNode(2), TreeNode(3))),
            TreeNode(1, TreeNode(2), TreeNode(10, TreeNode(2), TreeNode(20))),
            TreeNode(1, TreeNode(-1)),
            TreeNode(1, N.., TreeNode(2)),
            TreeNode(2, TreeNode(1, TreeNode(0), TreeNode(2, TreeNode(3))), TreeNode(3)),
        ]
        ___ root __ testCases:
            result = self.checkEqualTree(root)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
