'''
Created on Sep 4, 2017

@author: MT
'''
c_ TreeNode(o..
    ___ - , folder_ N..
        folder = folder
        content = ''
        children    # dict
        childFolders    # list
        isFile = F..

c_ FileSystem(o..
    ___ -
        root = TreeNode()
    
    ___ ls  p..
        p.. = p..[1:]
        arr = p...s..('/')
        __ arr[0] __ '':
            arr    # list
        node = root
        ___ folder __ arr:
            node = node.children[folder]
        node.childFolders.s..()
        __ node.isFile:
            r.. [node.folder]
        ____
            r.. node.childFolders
    
    ___ mkdir  p..
        p.. = p..[1:]
        arr = p...s..('/')
        node = root
        ___ folder __ arr:
            __ folder __ node.children:
                node = node.children[folder]
            ____
                newNode = TreeNode(folder)
                node.children[folder] = newNode
                node.childFolders.a..(folder)
                node = newNode
    
    ___ addContentToFile  filePath, content
        filePath = filePath[1:]
        arr = filePath.s..('/')
        file = arr[-1]
        arr = arr[:-1]
        node = root
        ___ folder __ arr:
            __ folder __ node.children:
                node = node.children[folder]
            ____
                newNode = TreeNode(folder)
                node.children[folder] = newNode
                node.childFolders.a..(folder)
                node = newNode
        __ file __ node.children:
            node.children[file].content += content
        ____
            newNode = TreeNode(file)
            node.children[file] = newNode
            node.childFolders.a..(file)
            newNode.isFile = T..
            newNode.content += content
    
    ___ readContentFromFile  filePath
        filePath = filePath[1:]
        arr = filePath.s..('/')
        node = root
        ___ folder __ arr:
            node = node.children[folder]
        r.. node.content
