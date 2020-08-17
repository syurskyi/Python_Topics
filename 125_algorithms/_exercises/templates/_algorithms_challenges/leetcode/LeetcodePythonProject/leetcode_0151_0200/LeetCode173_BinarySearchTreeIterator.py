'''
Created on Feb 14, 2017

@author: MT
'''

# Definition for a  binary tree node
class TreeNode(object
    ___ __init__(self, x
        self.val = x
        self.left = None
        self.right = None

class BSTIterator(object
    ___ __init__(self, root
        """
        :type root: TreeNode
        """
        self.stack = []
        __ root:
            self.stack.append(root)
            w___ root.left:
                root = root.left
                self.stack.append(root)

    ___ hasNext(self
        """
        :rtype: bool
        """
        r_ le.(self.stack) != 0
    
    ___ next(self
        """
        :rtype: int
        """
        node = self.stack.p..
        val = node.val
        __ node.right:
            node = node.right
            self.stack.append(node)
            w___ node.left:
                node = node.left
                self.stack.append(node)
        r_ val
