'''
Created on Feb 21, 2017

@author: MT
'''

# Definition for a binary tree node.
c_ TreeNode(o..
    ___ - , x, left=N.., right_ N..
        val = x
        left = left
        right = right

c_ Solution(o..
    ___ countNodes  root
        """
        :type root: TreeNode
        :rtype: int
        """
        _______ m__
        __ n.. root: r.. 0
        leftHeight = getLeftHeight(root)
        rightHeight = getRightHeight(root)
        __ leftHeight __ rightHeight:
            r.. i..(m__.pow(2, leftHeight)) - 1
        ____:
            r.. countNodes(root.left) + countNodes(root.right) + 1
    
    ___ getLeftHeight  root
        height = 0
        node = root
        w.... node:
            node = node.left
            height += 1
        r.. height
    
    ___ getRightHeight  root
        height = 0
        node = root
        w.... node:
            node = node.right
            height += 1
        r.. height
