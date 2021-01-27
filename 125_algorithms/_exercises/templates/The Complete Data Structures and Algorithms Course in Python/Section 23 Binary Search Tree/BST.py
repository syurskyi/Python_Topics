#   Created by Elshad Karimov 
#   Copyright © 2020 AppMillers. All rights reserved.

import QueueLinkedList as queue

class BSTNode:
    ___ __init__(self, data
        self.data = data
        self.leftChild = None
        self.rightChild = None

___ insertNode(rootNode, nodeValue
    __ rootNode.data == None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        __ rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(nodeValue)
        ____
            insertNode(rootNode.leftChild, nodeValue)
    ____
        __ rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(nodeValue)
        ____
            insertNode(rootNode.rightChild, nodeValue)
    return "The node has been successfully inserted"

___ preOrderTraversal(rootNode
    __ not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

___ inOrderTraversal(rootNode
    __ not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

___ postOrderTraversal(rootNode
    __ not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

___ levelOrderTraversal(rootNode
    __ not rootNode:
        return
    ____
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            __ root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            __ root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
            

___ searchNode(rootNode, nodeValue
    __ rootNode.data == nodeValue:
        print("The value is found")
    elif nodeValue < rootNode.data:
        __ rootNode.leftChild.data == nodeValue:
            print("The value is found")
        ____
            searchNode(rootNode.leftChild, nodeValue)
    ____
        __ rootNode.rightChild.data == nodeValue:
            print("The value is found")
        ____
            searchNode(rootNode.rightChild, nodeValue)


___ minValueNode(bstNode
    current = bstNode
    while (current.leftChild is not None
        current = current.leftChild
    return current


___ deleteNode(rootNode, nodeValue
    __ rootNode is None:
        return rootNode
    __ nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
    ____
        __ rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        
        __ rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp
        
        temp = minValueNode(rootNode.rightChild)
        rootNode.data = temp.data 
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)
    return rootNode

___ deleteBST(rootNode
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "The BST has been successfully deleted"



newBST = BSTNode(None)
insertNode(newBST, 70)
insertNode(newBST,50)
insertNode(newBST,90)
insertNode(newBST, 30)
insertNode(newBST,60)
insertNode(newBST,80)
insertNode(newBST,100)
insertNode(newBST,20)
insertNode(newBST,40)
print(deleteBST(newBST))
levelOrderTraversal(newBST)

