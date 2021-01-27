#   Created by Elshad Karimov 
#   Copyright © 2021 AppMillers. All rights reserved.

import QueueLinkedList as queue

class AVLNode:
    ___ __init__(self, data
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1

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

___ getHeight(rootNode
    __ not rootNode:
        return 0
    return rootNode.height

___ rightRotate(disbalanceNode
    newRoot = disbalanceNode.leftChild
    disbalanceNode.leftChild = disbalanceNode.leftChild.rightChild
    newRoot.rightChild = disbalanceNode
    disbalanceNode.height = 1 + max(getHeight(disbalanceNode.leftChild), getHeight(disbalanceNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    return newRoot

___ leftRotate(disbalanceNode
    newRoot = disbalanceNode.rightChild
    disbalanceNode.rightChild = disbalanceNode.rightChild.leftChild
    newRoot.leftChild = disbalanceNode
    disbalanceNode.height = 1 + max(getHeight(disbalanceNode.leftChild), getHeight(disbalanceNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    return newRoot

___ getBalance(rootNode
    __ not rootNode:
        return 0
    return getHeight(rootNode.leftChild) - getHeight(rootNode.rightChild)

___ insertNode(rootNode, nodeValue
    __ not rootNode:
        return AVLNode(nodeValue)
    elif nodeValue < rootNode.data:
        rootNode.leftChild = insertNode(rootNode.leftChild, nodeValue)
    ____
        rootNode.rightChild = insertNode(rootNode.rightChild, nodeValue)
    
    rootNode.height = 1 + max(getHeight(rootNode.leftChild), getHeight(rootNode.rightChild))
    balance = getBalance(rootNode)
    __ balance > 1 and nodeValue < rootNode.leftChild.data:
        return rightRotate(rootNode)
    __ balance > 1 and nodeValue > rootNode.leftChild.data:
        rootNode.leftChild = leftRotate(rootNode.leftChild)
        return rightRotate(rootNode)
    __ balance < -1 and nodeValue > rootNode.rightChild.data:
        return leftRotate(rootNode)
    __ balance < -1 and nodeValue < rootNode.rightChild.data:
        rootNode.rightChild = rightRotate(rootNode.rightChild)
        return leftRotate(rootNode)
    return rootNode

___ getMinValueNode(rootNode
    __ rootNode is None or rootNode.leftChild is None:
        return rootNode
    return getMinValueNode(rootNode.leftChild)

___ deleteNode(rootNode, nodeValue
    __ not rootNode:
        return rootNode
    elif nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
    ____
        __ rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        elif rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp
        temp = getMinValueNode(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)
    balance = getBalance(rootNode)
    __ balance > 1 and getBalance(rootNode.leftChild) >= 0:
        return rightRotate(rootNode)
    __ balance < -1 and getBalance(rootNode.rightChild) <= 0:
        return leftRotate(rootNode)
    __ balance > 1 and getBalance(rootNode.leftChild) < 0:
        rootNode.leftChild = leftRotate(rootNode.leftChild)
        return rightRotate(rootNode)
    __ balance < -1 and getBalance(rootNode.rightChild) > 0:
        rootNode.rightChild = rightRotate(rootNode.rightChild)
        return leftRotate(rootNode)
    
    return rootNode

___ deleteAVL(rootNode
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "The AVL has been successfully deleted"



newAVL = AVLNode(5)
newAVL = insertNode(newAVL, 10)
newAVL = insertNode(newAVL, 15)
newAVL = insertNode(newAVL, 20)
deleteAVL(newAVL)
levelOrderTraversal(newAVL)
