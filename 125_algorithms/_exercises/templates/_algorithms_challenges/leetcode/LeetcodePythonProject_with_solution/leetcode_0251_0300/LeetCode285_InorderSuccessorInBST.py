'''
Created on Mar 6, 2017

@author: MT
'''

# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x, left=N.., right_ N..
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    ___ inorderSuccessor(self, root, p):
        __ n.. root: r.. N..
        __ root.val <= p.val:
            r.. self.inorderSuccessor(root.right, p)
        ____:
            left = self.inorderSuccessor(root.left, p)
            __ left:
                r.. left
            ____:
                r.. root
    
    ___ inorderSuccessorNonRec(self, root, p):
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
                break
        w.... stack a.. stack[-1].val < p.val:
            stack.pop()
        __ n.. stack:
            r.. N..
        node = stack[-1]
        r.. node
