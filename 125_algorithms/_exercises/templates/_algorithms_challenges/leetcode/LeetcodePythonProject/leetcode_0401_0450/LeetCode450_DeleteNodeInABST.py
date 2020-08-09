'''
Created on Apr 20, 2017

@author: MT
'''

class Solution(object
    ___ deleteNode(self, root, key
        __ not root: r_ None
        parent, node = self.findNode(key, root, None)
        __ not node: r_ root
        __ not parent:
            r_ self.removeNode(node)
        ____
            newNode = self.removeNode(node)
            __ node __ parent.left:
                parent.left = newNode
            ____
                parent.right = newNode
            r_ root
    
    ___ removeNode(self, node
        __ node.right:
            newRoot = node.right
            left = node.left
            node = newRoot
            w___ node.left:
                node = node.left
            node.left = left
            r_ newRoot
        ____ node.left:
            newRoot = node.left
            right = node.right
            node = newRoot
            w___ node.right:
                node = node.right
            node.right = right
            r_ newRoot
        ____
            r_ None
    
    ___ findNode(self, key, root, parent
        __ not root:
            r_ None, None
        __ root.val __ key:
            r_ parent, root
        ____ root.val > key:
            r_ self.findNode(key, root.left, root)
        ____
            r_ self.findNode(key, root.right, root)
