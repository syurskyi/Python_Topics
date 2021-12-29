'''
Created on Mar 6, 2017

@author: MT
'''

# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x, left=None, right_ N..
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    ___ inorderSuccessor(self, root, p):
        __ not root: return None
        __ root.val <= p.val:
            return self.inorderSuccessor(root.right, p)
        else:
            left = self.inorderSuccessor(root.left, p)
            __ left:
                return left
            else:
                return root
    
    ___ inorderSuccessorNonRec(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        __ p.right:
            node = p.right
            while node.left:
                node = node.left
            return node.val
        stack = []
        node = root
        while node != p:
            stack.append(node)
            __ node.val > p.val:
                node = node.left
            elif node.val < p.val:
                node = node.right
            else:
                break
        while stack and stack[-1].val < p.val:
            stack.pop()
        __ not stack:
            return None
        node = stack[-1]
        return node
