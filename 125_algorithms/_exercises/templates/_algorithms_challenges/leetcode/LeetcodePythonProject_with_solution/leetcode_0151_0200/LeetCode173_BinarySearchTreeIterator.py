'''
Created on Feb 14, 2017

@author: MT
'''

# Definition for a  binary tree node
class TreeNode(object):
    ___ __init__(self, x):
        self.val = x
        self.left = N..
        self.right = N..

class BSTIterator(object):
    ___ __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack    # list
        __ root:
            self.stack.a..(root)
            w.... root.left:
                root = root.left
                self.stack.a..(root)

    ___ hasNext(self):
        """
        :rtype: bool
        """
        r.. l..(self.stack) != 0
    
    ___ next(self):
        """
        :rtype: int
        """
        node = self.stack.pop()
        val = node.val
        __ node.right:
            node = node.right
            self.stack.a..(node)
            w.... node.left:
                node = node.left
                self.stack.a..(node)
        r.. val
