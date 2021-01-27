#   Created by Elshad Karimov 
#   Copyright © 2020 AppMillers. All rights reserved.

class BinaryTree:
    ___ __init__(self, size
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size
    
    ___ insertNode(self, value
        __ self.lastUsedIndex + 1 == self.maxSize:
            r_ "The Binary Tree is full"
        self.customList[self.lastUsedIndex+1] = value
        self.lastUsedIndex += 1
        r_ "The value has been successfully inserted"

    ___ searchNode(self, nodeValue
        ___ i __ range(le_(self.customList)):
            __ self.customList[i] == nodeValue:
                r_ "Success"
        r_ "Not found"
    
    ___ preOrderTraversal(self, index
        __ index > self.lastUsedIndex:
            r_
        print(self.customList[index])
        self.preOrderTraversal(index*2)
        self.preOrderTraversal(index*2 + 1)

    ___ inOrderTraversal(self, index
        __ index > self.lastUsedIndex:
            r_
        self.inOrderTraversal(index*2)
        print(self.customList[index])
        self.inOrderTraversal(index*2+1)
    
    ___ postOrderTraversal(self, index
        __ index > self.lastUsedIndex:
            r_
        self.postOrderTraversal(index*2)
        self.postOrderTraversal(index*2+1)
        print(self.customList[index])
    
    ___ levelOrderTraversal(self, index
        ___ i __ range(index, self.lastUsedIndex+1
            print(self.customList[i])
    
    ___ deleteNode(self, value
        __ self.lastUsedIndex == 0:
            r_ "There is not any node to delete"
        ___ i __ range(1, self.lastUsedIndex+1
            __ self.customList[i] == value:
                self.customList[i] = self.customList[self.lastUsedIndex]
                self.customList[self.lastUsedIndex] = None
                self.lastUsedIndex -= 1
                r_ "The node has been successfully deleted"
    
    ___ deleteBT(self
       self.customList = None
       r_ "The BT has been successfully deleted"

    
 

newBT = BinaryTree(8)
newBT.insertNode("Drinks")
newBT.insertNode("Hot")
newBT.insertNode("Cold")
newBT.insertNode("Tea")
newBT.insertNode("Coffee")

print(newBT.deleteBT())

newBT.levelOrderTraversal(1)



