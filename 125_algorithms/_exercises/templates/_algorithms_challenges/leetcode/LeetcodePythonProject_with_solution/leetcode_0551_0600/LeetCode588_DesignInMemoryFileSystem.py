'''
Created on Sep 4, 2017

@author: MT
'''
class TreeNode(object):
    ___ __init__(self, folder_ N..
        self.folder = folder
        self.content = ''
        self.children = {}
        self.childFolders    # list
        self.isFile = False

class FileSystem(object):
    ___ __init__(self):
        self.root = TreeNode()
    
    ___ ls(self, path):
        path = path[1:]
        arr = path.split('/')
        __ arr[0] __ '':
            arr    # list
        node = self.root
        ___ folder __ arr:
            node = node.children[folder]
        node.childFolders.sort()
        __ node.isFile:
            r.. [node.folder]
        ____:
            r.. node.childFolders
    
    ___ mkdir(self, path):
        path = path[1:]
        arr = path.split('/')
        node = self.root
        ___ folder __ arr:
            __ folder __ node.children:
                node = node.children[folder]
            ____:
                newNode = TreeNode(folder)
                node.children[folder] = newNode
                node.childFolders.a..(folder)
                node = newNode
    
    ___ addContentToFile(self, filePath, content):
        filePath = filePath[1:]
        arr = filePath.split('/')
        file = arr[-1]
        arr = arr[:-1]
        node = self.root
        ___ folder __ arr:
            __ folder __ node.children:
                node = node.children[folder]
            ____:
                newNode = TreeNode(folder)
                node.children[folder] = newNode
                node.childFolders.a..(folder)
                node = newNode
        __ file __ node.children:
            node.children[file].content += content
        ____:
            newNode = TreeNode(file)
            node.children[file] = newNode
            node.childFolders.a..(file)
            newNode.isFile = True
            newNode.content += content
    
    ___ readContentFromFile(self, filePath):
        filePath = filePath[1:]
        arr = filePath.split('/')
        node = self.root
        ___ folder __ arr:
            node = node.children[folder]
        r.. node.content
