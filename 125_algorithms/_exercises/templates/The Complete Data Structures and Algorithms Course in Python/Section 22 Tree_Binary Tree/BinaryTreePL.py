#   Created by Elshad Karimov 
#   Copyright © 2020 AppMillers. All rights reserved.

class BinaryTree:
    ___ __init__(self, size
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size
    
    ___ insertNode(self, value
        __ self.lastUsedIndex + 1 == self.maxSize:
            return "The Binary Tree is full"
        self.customList[self.lastUsedIndex+1] = value
        self.lastUsedIndex += 1
        return "The value has been successfully inserted"

    ___ searchNode(self, nodeValue
        for i in range(len(self.customList)):
            __ self.customList[i] == nodeValue:
                return "Success"
        return "Not found"
    
    ___ preOrderTraversal(self, index
        __ index > self.lastUsedIndex:
            return
        print(self.customList[index])
        self.preOrderTraversal(index*2)
        self.preOrderTraversal(index*2 + 1)

    ___ inOrderTraversal(self, index
        __ index > self.lastUsedIndex:
            return
        self.inOrderTraversal(index*2)
        print(self.customList[index])
        self.inOrderTraversal(index*2+1)
    
    ___ postOrderTraversal(self, index
        __ index > self.lastUsedIndex:
            return
        self.postOrderTraversal(index*2)
        self.postOrderTraversal(index*2+1)
        print(self.customList[index])
    
    ___ levelOrderTraversal(self, index
        for i in range(index, self.lastUsedIndex+1
            print(self.customList[i])
    
    ___ deleteNode(self, value
        __ self.lastUsedIndex == 0:
            return "There is not any node to delete"
        for i in range(1, self.lastUsedIndex+1
            __ self.customList[i] == value:
                self.customList[i] = self.customList[self.lastUsedIndex]
                self.customList[self.lastUsedIndex] = None
                self.lastUsedIndex -= 1
                return "The node has been successfully deleted"
    
    ___ deleteBT(self
       self.customList = None
       return "The BT has been successfully deleted"

    
 

newBT = BinaryTree(8)
newBT.insertNode("Drinks")
newBT.insertNode("Hot")
newBT.insertNode("Cold")
newBT.insertNode("Tea")
newBT.insertNode("Coffee")

print(newBT.deleteBT())

newBT.levelOrderTraversal(1)



