'''
Created on Mar 19, 2017

@author: MT
'''
# Definition for a binary tree node.
c_ TreeNode(o..
    ___ - , x
        val x
        left N..
        right N..

c_ Solution(o..
    ___ largestBSTSubtree  root
        r.. helper(root)[-1]
    
    #isBST, lower, upper, count
    ___ helper  root
        __ n.. root:
            r.. T.., f__('inf'), f__('-inf'), 0
        leftBST, leftLower, leftUpper, leftCount helper(root.left)
        rightBST, rightLower, rightUpper, rightCount helper(root.right)
        lower m..(leftLower, root.val)
        upper m..(rightUpper, root.val)
        __ leftBST a.. rightBST a.. leftUpper < root.val < rightLower:
            r.. T.., lower, upper, 1+leftCount+rightCount
        ____
            r.. F.., lower, upper, m..(leftCount, rightCount)
    