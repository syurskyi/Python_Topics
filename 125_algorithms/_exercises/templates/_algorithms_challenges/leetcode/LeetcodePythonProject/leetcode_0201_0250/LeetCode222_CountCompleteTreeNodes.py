'''
Created on Feb 21, 2017

@author: MT
'''

# Definition for a binary tree node.
class TreeNode(object
    ___ __init__(self, x, left=None, right=None
        self.val = x
        self.left = left
        self.right = right

class Solution(object
    ___ countNodes(self, root
        """
        :type root: TreeNode
        :rtype: int
        """
        ______ ma__
        __ not root: r_ 0
        leftHeight = self.getLeftHeight(root)
        rightHeight = self.getRightHeight(root)
        __ leftHeight __ rightHeight:
            r_ int(ma__.pow(2, leftHeight)) - 1
        ____
            r_ self.countNodes(root.left) + self.countNodes(root.right) + 1
    
    ___ getLeftHeight(self, root
        height = 0
        node = root
        w___ node:
            node = node.left
            height += 1
        r_ height
    
    ___ getRightHeight(self, root
        height = 0
        node = root
        w___ node:
            node = node.right
            height += 1
        r_ height
