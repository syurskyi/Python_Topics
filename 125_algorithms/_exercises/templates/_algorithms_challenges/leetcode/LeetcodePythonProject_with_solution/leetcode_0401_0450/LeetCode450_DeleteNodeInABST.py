'''
Created on Apr 20, 2017

@author: MT
'''

class Solution(object):
    ___ deleteNode(self, root, key):
        __ n.. root: r.. N..
        parent, node = self.findNode(key, root, N..)
        __ n.. node: r.. root
        __ n.. parent:
            r.. self.removeNode(node)
        ____:
            newNode = self.removeNode(node)
            __ node __ parent.left:
                parent.left = newNode
            ____:
                parent.right = newNode
            r.. root
    
    ___ removeNode(self, node):
        __ node.right:
            newRoot = node.right
            left = node.left
            node = newRoot
            w.... node.left:
                node = node.left
            node.left = left
            r.. newRoot
        ____ node.left:
            newRoot = node.left
            right = node.right
            node = newRoot
            w.... node.right:
                node = node.right
            node.right = right
            r.. newRoot
        ____:
            r.. N..
    
    ___ findNode(self, key, root, parent):
        __ n.. root:
            r.. N.., N..
        __ root.val __ key:
            r.. parent, root
        ____ root.val > key:
            r.. self.findNode(key, root.left, root)
        ____:
            r.. self.findNode(key, root.right, root)
