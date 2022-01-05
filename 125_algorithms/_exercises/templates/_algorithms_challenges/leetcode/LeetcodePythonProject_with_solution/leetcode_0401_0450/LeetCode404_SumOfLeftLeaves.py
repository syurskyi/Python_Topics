'''
Created on Apr 9, 2017

@author: MT
'''

# Definition for a binary tree node.
c_ TreeNode(o..):
    ___ - , x, left=N.., right_ N..
        val = x
        left = left
        right = right

c_ Solution(o..):
    ___ sumOfLeftLeaves  root):
        __ n.. root: r.. 0
        sumVal = 0
        __ root.left:
            __ n.. root.left.left a.. n.. root.left.right:
                sumVal += root.left.val
            ____:
                sumVal += sumOfLeftLeaves(root.left)
        __ root.right:
            sumVal += sumOfLeftLeaves(root.right)
        r.. sumVal
    
    