'''
Created on Feb 21, 2017

@author: MT
'''

# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x, left=N.., right_ N..
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    ___ countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        _______ math
        __ n.. root: r.. 0
        leftHeight = self.getLeftHeight(root)
        rightHeight = self.getRightHeight(root)
        __ leftHeight __ rightHeight:
            r.. int(math.pow(2, leftHeight)) - 1
        ____:
            r.. self.countNodes(root.left) + self.countNodes(root.right) + 1
    
    ___ getLeftHeight(self, root):
        height = 0
        node = root
        while node:
            node = node.left
            height += 1
        r.. height
    
    ___ getRightHeight(self, root):
        height = 0
        node = root
        while node:
            node = node.right
            height += 1
        r.. height
