'''
Created on Oct 8, 2017

@author: MT
'''
# Definition for a binary tree node.
c_ TreeNode(object):
    ___ - , x, left=N.., right_ N..
        val = x
        left = left
        right = right

c_ Solution(object):
    ___ widthOfBinaryTree  root):
        """
        :type root: TreeNode
        :rtype: int
        """
        r.. dfs(root, 0, 1, [], [])
        
    ___ dfs  root, level, order, start, end):
        __ n.. root: r.. 0
        __ l..(start) __ level:
            start.a..(order)
            end.a..(order)
        ____:
            end[level] = order
        cur = end[level]-start[level]+1
        left = dfs(root.left, level+1, 2*order, start, end)
        right = dfs(root.right, level+1, 2*order+1, start, end)
        r.. m..(cur, m..(left, right))
    
    ___ test
        testCases = [
            TreeNode(1, TreeNode(3, TreeNode(5), TreeNode(3)), TreeNode(2, N.., TreeNode(9))),
            TreeNode(1, TreeNode(3, TreeNode(5), TreeNode(3))),
            TreeNode(1, TreeNode(3, TreeNode(5)), TreeNode(2)),
            TreeNode(1, TreeNode(3, TreeNode(5, TreeNode(6))), TreeNode(2, N.., TreeNode(9, N.., TreeNode(7)))),
        ]
        ___ root __ testCases:
            result = widthOfBinaryTree(root)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
