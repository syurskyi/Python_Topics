'''
Created on Mar 4, 2017

@author: MT
'''

# Definition for a binary tree node.
c_ TreeNode(o..
    ___ - , x, left=N.., right_ N..
        val = x
        left = left
        right = right

c_ Solution(o..
    ___ closestValue  root, target
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        result= root.val
        w.... root:
            __ abs(target - root.val) < abs(target-result
                result = root.val
            __ root.val > target:
                root = root.left
            ____
                root = root.right
        r.. result
