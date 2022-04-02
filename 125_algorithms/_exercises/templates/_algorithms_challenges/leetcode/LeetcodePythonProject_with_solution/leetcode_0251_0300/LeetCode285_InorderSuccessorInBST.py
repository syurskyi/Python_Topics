'''
Created on Mar 6, 2017

@author: MT
'''

# Definition for a binary tree node.
c_ TreeNode(o..
    ___ - , x, left=N.., right_ N..
        val = x
        left = left
        right = right

c_ Solution(o..
    ___ inorderSuccessor  root, p
        __ n.. root: r.. N..
        __ root.val <= p.val:
            r.. inorderSuccessor(root.right, p)
        ____:
            left = inorderSuccessor(root.left, p)
            __ left:
                r.. left
            ____:
                r.. root
    
    ___ inorderSuccessorNonRec  root, p
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        __ p.right:
            node = p.right
            w.... node.left:
                node = node.left
            r.. node.val
        stack    # list
        node = root
        w.... node != p:
            stack.a..(node)
            __ node.val > p.val:
                node = node.left
            ____ node.val < p.val:
                node = node.right
            ____:
                _____
        w.... stack a.. stack[-1].val < p.val:
            stack.pop()
        __ n.. stack:
            r.. N..
        node = stack[-1]
        r.. node
