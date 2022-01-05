'''
Created on Feb 14, 2017

@author: MT
'''

# Definition for a  binary tree node
c_ TreeNode(o..):
    ___ - , x):
        val = x
        left = N..
        right = N..

c_ BSTIterator(o..):
    ___ - , root):
        """
        :type root: TreeNode
        """
        stack    # list
        __ root:
            stack.a..(root)
            w.... root.left:
                root = root.left
                stack.a..(root)

    ___ hasNext
        """
        :rtype: bool
        """
        r.. l..(stack) != 0
    
    ___ next
        """
        :rtype: int
        """
        node = stack.pop()
        val = node.val
        __ node.right:
            node = node.right
            stack.a..(node)
            w.... node.left:
                node = node.left
                stack.a..(node)
        r.. val
