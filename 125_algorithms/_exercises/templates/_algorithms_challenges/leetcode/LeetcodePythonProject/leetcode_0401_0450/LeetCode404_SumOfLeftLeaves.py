'''
Created on Apr 9, 2017

@author: MT
'''

# Definition for a binary tree node.
class TreeNode(object
    ___ __init__(self, x, left=None, right=None
        self.val = x
        self.left = left
        self.right = right

class Solution(object
    ___ sumOfLeftLeaves(self, root
        __ not root: r_ 0
        sumVal = 0
        __ root.left:
            __ not root.left.left and not root.left.right:
                sumVal += root.left.val
            ____
                sumVal += self.sumOfLeftLeaves(root.left)
        __ root.right:
            sumVal += self.sumOfLeftLeaves(root.right)
        r_ sumVal
    
    