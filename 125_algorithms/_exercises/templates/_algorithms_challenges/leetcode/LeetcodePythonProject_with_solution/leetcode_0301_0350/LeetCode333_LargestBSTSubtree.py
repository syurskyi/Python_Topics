'''
Created on Mar 19, 2017

@author: MT
'''
# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    ___ largestBSTSubtree(self, root):
        return self.helper(root)[-1]
    
    #isBST, lower, upper, count
    ___ helper(self, root):
        __ not root:
            return True, float('inf'), float('-inf'), 0
        leftBST, leftLower, leftUpper, leftCount = self.helper(root.left)
        rightBST, rightLower, rightUpper, rightCount = self.helper(root.right)
        lower = min(leftLower, root.val)
        upper = max(rightUpper, root.val)
        __ leftBST and rightBST and leftUpper < root.val < rightLower:
            return True, lower, upper, 1+leftCount+rightCount
        else:
            return False, lower, upper, max(leftCount, rightCount)
    