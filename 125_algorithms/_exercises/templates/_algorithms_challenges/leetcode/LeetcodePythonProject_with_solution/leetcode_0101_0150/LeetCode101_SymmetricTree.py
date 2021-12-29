'''
Created on Jan 31, 2017

@author: MT
'''

# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x, left=None, right_ N..
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    ___ isSymmetricRecursive(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        __ not root: return True
        return self.helper(root.left, root.left)
    
    ___ helper(self, left, right):
        __ not left and not right:
            return True
        elif not left or not right:
            return False
        elif left.val != right.val:
            return False
        else:
            return self.helper(left.left, right.right) and\
                self.helper(left.right, right.left)
    
    ___ isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        __ not root: return True
        stack = []
        __ root.left:
            __ not root.right: return False
            stack.append(root.left)
            stack.append(root.right)
        elif root.right:
            return False
        while stack:
            __ len(stack)%2 != 0:
                return False
            right = stack.pop()
            left = stack.pop()
            __ right.val != left.val:
                return False
            __ left.left:
                __ not right.right:
                    return False
                stack.append(left.left)
                stack.append(right.right)
            elif right.right:
                return False
            __ left.right:
                __ not right.left:
                    return False
                stack.append(left.right)
                stack.append(right.left)
            elif right.left:
                return False
        return True
        