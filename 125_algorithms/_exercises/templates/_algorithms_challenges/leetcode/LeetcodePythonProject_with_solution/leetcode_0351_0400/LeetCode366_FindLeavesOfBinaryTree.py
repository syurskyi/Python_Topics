'''
Created on Mar 28, 2017

@author: MT
'''

# Definition for a binary tree node.
c_ TreeNode(object):
    ___ - , x, left=N.., right_ N..
        val = x
        left = left
        right = right

c_ Solution(object):
    ___ findLeaves(self, root):
        res    # list
        helper(root, res)
        r.. res
    
    ___ helper(self, root, res):
        __ n.. root: r.. -1
        left = helper(root.left, res)
        right = helper(root.right, res)
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
        w.... dummy.left:
            tmpResult    # list
            getLeaves(dummy, root, tmpResult)
            result.a..(tmpResult)
        r.. result
    
    ___ getLeaves(self, parent, root, result):
        __ n.. root: r..
        __ n.. root.left a.. n.. root.right:
            __ parent.left __ root:
                parent.left = N..
            ____:
                parent.right = N..
            result.a..(root.val)
        getLeaves(root, root.left, result)
        getLeaves(root, root.right, result)
    
    ___ test
        testCases = [
            TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3)),
        ]
        ___ root __ testCases:
            result = findLeaves(root)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
