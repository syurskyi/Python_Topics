'''
Created on Feb 14, 2017

@author: MT
'''

# Definition for a  binary tree node
class TreeNode(object):
    ___ __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator(object):
    ___ __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        __ root:
            self.stack.append(root)
            while root.left:
                root = root.left
                self.stack.append(root)

    ___ hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) != 0
    
    ___ next(self):
        """
        :rtype: int
        """
        node = self.stack.pop()
        val = node.val
        __ node.right:
            node = node.right
            self.stack.append(node)
            while node.left:
                node = node.left
                self.stack.append(node)
        return val
