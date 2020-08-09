'''
Created on Mar 4, 2017

@author: MT
'''

# Definition for a binary tree node.
class TreeNode(object
    ___ __init__(self, x, left=None, right=None
        self.val = x
        self.left = left
        self.right = right

class Solution(object
    ___ closestValue(self, root, target
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        result= root.val
        w___ root:
            __ abs(target - root.val) < abs(target-result
                result = root.val
            __ root.val > target:
                root = root.left
            ____
                root = root.right
        r_ result
