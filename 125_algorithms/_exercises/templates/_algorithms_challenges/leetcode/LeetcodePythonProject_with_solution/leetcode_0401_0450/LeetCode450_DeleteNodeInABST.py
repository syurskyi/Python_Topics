'''
Created on Apr 20, 2017

@author: MT
'''

c_ Solution(o..
    ___ deleteNode  root, key
        __ n.. root: r.. N..
        parent, node = findNode(key, root, N..)
        __ n.. node: r.. root
        __ n.. parent:
            r.. removeNode(node)
        ____
            newNode = removeNode(node)
            __ node __ parent.left:
                parent.left = newNode
            ____
                parent.right = newNode
            r.. root
    
    ___ removeNode  node
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
        ____
            r.. N..
    
    ___ findNode  key, root, parent
        __ n.. root:
            r.. N.., N..
        __ root.val __ key:
            r.. parent, root
        ____ root.val > key:
            r.. findNode(key, root.left, root)
        ____
            r.. findNode(key, root.right, root)
