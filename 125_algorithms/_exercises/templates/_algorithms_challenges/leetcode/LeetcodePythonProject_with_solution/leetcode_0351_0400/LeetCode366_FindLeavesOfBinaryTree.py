'''
Created on Mar 28, 2017

@author: MT
'''

# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x, left=N.., right_ N..
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    ___ findLeaves(self, root):
        res    # list
        self.helper(root, res)
        r.. res
    
    ___ helper(self, root, res):
        __ n.. root: r.. -1
        left = self.helper(root.left, res)
        right = self.helper(root.right, res)
        level = max(left, right)+1
        __ level < l..(res):
            res[level].a..(root.val)
        ____:
            res.a..([root.val])
        r.. level
    
    ___ findLeavesOwn(self, root):
        __ n.. root: r.. []
        result    # list
        dummy = TreeNode(-1)
        dummy.left = root
        while dummy.left:
            tmpResult    # list
            self.getLeaves(dummy, root, tmpResult)
            result.a..(tmpResult)
        r.. result
    
    ___ getLeaves(self, parent, root, result):
        __ n.. root: r..
        __ n.. root.left and n.. root.right:
            __ parent.left __ root:
                parent.left = N..
            ____:
                parent.right = N..
            result.a..(root.val)
        self.getLeaves(root, root.left, result)
        self.getLeaves(root, root.right, result)
    
    ___ test(self):
        testCases = [
            TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3)),
        ]
        ___ root __ testCases:
            result = self.findLeaves(root)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
