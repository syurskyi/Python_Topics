'''
Created on Mar 19, 2017

@author: MT
'''
# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x):
        self.val = x
        self.left = N..
        self.right = N..

class Solution(object):
    ___ largestBSTSubtree(self, root):
        r.. self.helper(root)[-1]
    
    #isBST, lower, upper, count
    ___ helper(self, root):
        __ n.. root:
            r.. True, float('inf'), float('-inf'), 0
        leftBST, leftLower, leftUpper, leftCount = self.helper(root.left)
        rightBST, rightLower, rightUpper, rightCount = self.helper(root.right)
        lower = m..(leftLower, root.val)
        upper = max(rightUpper, root.val)
        __ leftBST a.. rightBST a.. leftUpper < root.val < rightLower:
            r.. True, lower, upper, 1+leftCount+rightCount
        ____:
            r.. False, lower, upper, max(leftCount, rightCount)
    