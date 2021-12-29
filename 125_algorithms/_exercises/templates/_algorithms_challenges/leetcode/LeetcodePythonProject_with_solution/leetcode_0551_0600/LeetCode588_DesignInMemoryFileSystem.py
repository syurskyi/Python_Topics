'''
Created on Sep 4, 2017

@author: MT
'''
class TreeNode(object):
    ___ __init__(self, folder_ N..
        self.folder = folder
        self.content = ''
        self.children = {}
        self.childFolders = []
        self.isFile = False

class FileSystem(object):
    ___ __init__(self):
        self.root = TreeNode()
    
    ___ ls(self, path):
        path = path[1:]
        arr = path.split('/')
        __ arr[0] == '':
            arr = []
        node = self.root
        for folder in arr:
            node = node.children[folder]
        node.childFolders.sort()
        __ node.isFile:
            return [node.folder]
        else:
            return node.childFolders
    
    ___ mkdir(self, path):
        path = path[1:]
        arr = path.split('/')
        node = self.root
        for folder in arr:
            __ folder in node.children:
                node = node.children[folder]
            else:
                newNode = TreeNode(folder)
                node.children[folder] = newNode
                node.childFolders.append(folder)
                node = newNode
    
    ___ addContentToFile(self, filePath, content):
        filePath = filePath[1:]
        arr = filePath.split('/')
        file = arr[-1]
        arr = arr[:-1]
        node = self.root
        for folder in arr:
            __ folder in node.children:
                node = node.children[folder]
            else:
                newNode = TreeNode(folder)
                node.children[folder] = newNode
                node.childFolders.append(folder)
                node = newNode
        __ file in node.children:
            node.children[file].content += content
        else:
            newNode = TreeNode(file)
            node.children[file] = newNode
            node.childFolders.append(file)
            newNode.isFile = True
            newNode.content += content
    
    ___ readContentFromFile(self, filePath):
        filePath = filePath[1:]
        arr = filePath.split('/')
        node = self.root
        for folder in arr:
            node = node.children[folder]
        return node.content
