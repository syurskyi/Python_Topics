#   Created by Elshad Karimov 
#   Copyright © 2021 AppMillers. All rights reserved.

class TrieNode:
    ___ __init__(self
        self.children = {}
        self.endOfString = False

class Trie:
    ___ __init__(self
        self.root = TrieNode()
    
    ___ insertString(self, word
        current = self.root
        for i in word:
            ch = i
            node = current.children.get(ch)
            __ node == None:
                node = TrieNode()
                current.children.update({ch:node})
            current = node
        current.endOfString = True
        print("Successfully inserted")
    
    ___ searchString(self, word
        currentNode = self.root
        for i in word:
            node = currentNode.children.get(i)
            __ node == None:
                return False
            currentNode = node

        __ currentNode.endOfString == True:
            return True
        ____
            return False
        

___ deleteString(root, word, index
    ch = word[index]
    currentNode = root.children.get(ch)
    canThisNodeBeDeleted = False

    __ len(currentNode.children) > 1:
        deleteString(currentNode, word, index+1)
        return False
    
    __ index == len(word) - 1:
        __ len(currentNode.children) >= 1:
            currentNode.endOfString = False
            return False
        ____
            root.children.pop(ch)
            return True
    
    __ currentNode.endOfString == True:
        deleteString(currentNode, word, index+1)
        return False

    canThisNodeBeDeleted = deleteString(currentNode, word, index+1)
    __ canThisNodeBeDeleted == True:
        root.children.pop(ch)
        return True
    ____
        return False



    
newTrie = Trie()
newTrie.insertString("App")
newTrie.insertString("Appl")
deleteString(newTrie.root, "App", 0)
print(newTrie.searchString("App"))