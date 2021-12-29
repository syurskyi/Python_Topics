'''
Created on Apr 9, 2017

@author: MT
'''

# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x, left=N.., right_ N..
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    ___ sumOfLeftLeaves(self, root):
        __ n.. root: r.. 0
        sumVal = 0
        __ root.left:
            __ n.. root.left.left a.. n.. root.left.right:
                sumVal += root.left.val
            ____:
                sumVal += self.sumOfLeftLeaves(root.left)
        __ root.right:
            sumVal += self.sumOfLeftLeaves(root.right)
        r.. sumVal
    
    