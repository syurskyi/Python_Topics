'''
Created on Apr 20, 2017

@author: MT
'''

class Solution(object):
    ___ deleteNode(self, root, key):
        __ not root: return None
        parent, node = self.findNode(key, root, None)
        __ not node: return root
        __ not parent:
            return self.removeNode(node)
        else:
            newNode = self.removeNode(node)
            __ node == parent.left:
                parent.left = newNode
            else:
                parent.right = newNode
            return root
    
    ___ removeNode(self, node):
        __ node.right:
            newRoot = node.right
            left = node.left
            node = newRoot
            while node.left:
                node = node.left
            node.left = left
            return newRoot
        elif node.left:
            newRoot = node.left
            right = node.right
            node = newRoot
            while node.right:
                node = node.right
            node.right = right
            return newRoot
        else:
            return None
    
    ___ findNode(self, key, root, parent):
        __ not root:
            return None, None
        __ root.val == key:
            return parent, root
        elif root.val > key:
            return self.findNode(key, root.left, root)
        else:
            return self.findNode(key, root.right, root)
