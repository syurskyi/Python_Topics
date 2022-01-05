'''
Created on Mar 9, 2017

@author: MT
'''

# Definition for a binary tree node.
c_ TreeNode(o..):
    ___ - , x, left=N.., right_ N..
        val = x
        left = left
        right = right

c_ Solution(o..):
    ___ longestConsecutive  root):
        __ n.. root: r.. 0
        result = [1]
        helper(root, 1, result)
        r.. result[0]
    
    ___ helper  root, length, result):
        __ n.. root.left a.. n.. root.right:
            result[0] = m..(result[0], length)
            r..
        __ root.left:
            __ root.left.val __ root.val+1:
                helper(root.left, length+1, result)
            ____:
                result[0] = m..(result[0], length)
                helper(root.left, 1, result)
        __ root.right:
            __ root.right.val __ root.val+1:
                helper(root.right, length+1, result)
            ____:
                result[0] = m..(result[0], length)
                helper(root.right, 1, result)
    
    ___ test
        root = TreeNode(1, N.., TreeNode(3, TreeNode(2), TreeNode(4, N.., TreeNode(5))))
        result = longestConsecutive(root)
        print('result: %s' % (result))

__ _____ __ _____
    Solution().test()

    