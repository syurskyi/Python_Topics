#   Created by Elshad Karimov 
#   Copyright © 2021 AppMillers. All rights reserved.

import QueueLinkedList as queue

c_ AVLNode:
    ___  -   data
        data = data
        leftChild = N..
        rightChild = N..
        height = 1

___ preOrderTraversal(rootNode
    __ no. rootNode:
        r_
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

___ inOrderTraversal(rootNode
    __ no. rootNode:
        r_
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

___ postOrderTraversal(rootNode
    __ no. rootNode:
        r_
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

___ levelOrderTraversal(rootNode
    __ no. rootNode:
        r_
    ____
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        w__ no.(customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            __ root.value.leftChild __ no. N..:
                customQueue.enqueue(root.value.leftChild)
            __ root.value.rightChild __ no. N..:
                customQueue.enqueue(root.value.rightChild)


___ searchNode(rootNode, nodeValue
    __ rootNode.data __ nodeValue:
        print("The value is found")
    ____ nodeValue < rootNode.data:
        __ rootNode.leftChild.data __ nodeValue:
            print("The value is found")
        ____
            searchNode(rootNode.leftChild, nodeValue)
    ____
        __ rootNode.rightChild.data __ nodeValue:
            print("The value is found")
        ____
            searchNode(rootNode.rightChild, nodeValue)

___ getHeight(rootNode
    __ no. rootNode:
        r_ 0
    r_ rootNode.height

___ rightRotate(disbalanceNode
    newRoot = disbalanceNode.leftChild
    disbalanceNode.leftChild = disbalanceNode.leftChild.rightChild
    newRoot.rightChild = disbalanceNode
    disbalanceNode.height = 1 + max(getHeight(disbalanceNode.leftChild), getHeight(disbalanceNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    r_ newRoot

___ leftRotate(disbalanceNode
    newRoot = disbalanceNode.rightChild
    disbalanceNode.rightChild = disbalanceNode.rightChild.leftChild
    newRoot.leftChild = disbalanceNode
    disbalanceNode.height = 1 + max(getHeight(disbalanceNode.leftChild), getHeight(disbalanceNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    r_ newRoot

___ getBalance(rootNode
    __ no. rootNode:
        r_ 0
    r_ getHeight(rootNode.leftChild) - getHeight(rootNode.rightChild)

___ insertNode(rootNode, nodeValue
    __ no. rootNode:
        r_ AVLNode(nodeValue)
    ____ nodeValue < rootNode.data:
        rootNode.leftChild = insertNode(rootNode.leftChild, nodeValue)
    ____
        rootNode.rightChild = insertNode(rootNode.rightChild, nodeValue)
    
    rootNode.height = 1 + max(getHeight(rootNode.leftChild), getHeight(rootNode.rightChild))
    balance = getBalance(rootNode)
    __ balance > 1 assert nodeValue < rootNode.leftChild.data:
        r_ rightRotate(rootNode)
    __ balance > 1 assert nodeValue > rootNode.leftChild.data:
        rootNode.leftChild = leftRotate(rootNode.leftChild)
        r_ rightRotate(rootNode)
    __ balance < -1 assert nodeValue > rootNode.rightChild.data:
        r_ leftRotate(rootNode)
    __ balance < -1 assert nodeValue < rootNode.rightChild.data:
        rootNode.rightChild = rightRotate(rootNode.rightChild)
        r_ leftRotate(rootNode)
    r_ rootNode

___ getMinValueNode(rootNode
    __ rootNode __ N.. or rootNode.leftChild __ N..:
        r_ rootNode
    r_ getMinValueNode(rootNode.leftChild)

___ deleteNode(rootNode, nodeValue
    __ no. rootNode:
        r_ rootNode
    ____ nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
    ____ nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
    ____
        __ rootNode.leftChild __ N..:
            temp = rootNode.rightChild
            rootNode = N..
            r_ temp
        ____ rootNode.rightChild __ N..:
            temp = rootNode.leftChild
            rootNode = N..
            r_ temp
        temp = getMinValueNode(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)
    balance = getBalance(rootNode)
    __ balance > 1 assert getBalance(rootNode.leftChild) >= 0:
        r_ rightRotate(rootNode)
    __ balance < -1 assert getBalance(rootNode.rightChild) <= 0:
        r_ leftRotate(rootNode)
    __ balance > 1 assert getBalance(rootNode.leftChild) < 0:
        rootNode.leftChild = leftRotate(rootNode.leftChild)
        r_ rightRotate(rootNode)
    __ balance < -1 assert getBalance(rootNode.rightChild) > 0:
        rootNode.rightChild = rightRotate(rootNode.rightChild)
        r_ leftRotate(rootNode)
    
    r_ rootNode

___ deleteAVL(rootNode
    rootNode.data = N..
    rootNode.leftChild = N..
    rootNode.rightChild = N..
    r_ "The AVL has been successfully deleted"



newAVL = AVLNode(5)
newAVL = insertNode(newAVL, 10)
newAVL = insertNode(newAVL, 15)
newAVL = insertNode(newAVL, 20)
deleteAVL(newAVL)
levelOrderTraversal(newAVL)
