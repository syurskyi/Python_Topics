#   Created by Elshad Karimov 
#   Copyright © 2021 AppMillers. All rights reserved.

c_ TrieNode:
    ___  - (self
        children  {}
        endOfString  F..

c_ Trie:
    ___  - (self
        root  TrieNode()
    
    ___ insertString  word
        current  root
        ___ i __ word:
            ch  i
            node  current.children.get(ch)
            __ node __ N..:
                node  TrieNode()
                current.children.update({ch:node})
            current  node
        current.endOfString  T..
        print("Successfully inserted")
    
    ___ searchString  word
        currentNode  root
        ___ i __ word:
            node  currentNode.children.get(i)
            __ node __ N..:
                r_ F..
            currentNode  node

        __ currentNode.endOfString __ T..:
            r_ T..
        ____
            r_ F..
        

___ deleteString(root, word, index
    ch  word[index]
    currentNode  root.children.get(ch)
    canThisNodeBeDeleted  F..

    __ le_(currentNode.children) > 1:
        deleteString(currentNode, word, index+1)
        r_ F..
    
    __ index __ le_(word) - 1:
        __ le_(currentNode.children) > 1:
            currentNode.endOfString  F..
            r_ F..
        ____
            root.children.pop(ch)
            r_ T..
    
    __ currentNode.endOfString __ T..:
        deleteString(currentNode, word, index+1)
        r_ F..

    canThisNodeBeDeleted  deleteString(currentNode, word, index+1)
    __ canThisNodeBeDeleted __ T..:
        root.children.pop(ch)
        r_ T..
    ____
        r_ F..



    
newTrie  Trie()
newTrie.insertString("App")
newTrie.insertString("Appl")
deleteString(newTrie.root, "App", 0)
print(newTrie.searchString("App"))