'''
Created on Mar 19, 2017

@author: MT
'''
# Definition for a binary tree node.
c_ TreeNode(object):
    ___ - , x):
        val = x
        left = N..
        right = N..

c_ Solution(object):
    ___ largestBSTSubtree(self, root):
        r.. helper(root)[-1]
    
    #isBST, lower, upper, count
    ___ helper(self, root):
        __ n.. root:
            r.. T.., float('inf'), float('-inf'), 0
        leftBST, leftLower, leftUpper, leftCount = helper(root.left)
        rightBST, rightLower, rightUpper, rightCount = helper(root.right)
        lower = m..(leftLower, root.val)
        upper = max(rightUpper, root.val)
        __ leftBST a.. rightBST a.. leftUpper < root.val < rightLower:
            r.. T.., lower, upper, 1+leftCount+rightCount
        ____:
            r.. F.., lower, upper, max(leftCount, rightCount)
    