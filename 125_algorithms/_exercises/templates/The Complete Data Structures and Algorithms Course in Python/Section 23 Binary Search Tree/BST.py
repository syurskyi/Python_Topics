#   Created by Elshad Karimov 
#   Copyright © 2020 AppMillers. All rights reserved.

_____ QueueLinkedList as queue

c_ BSTNode:
    ___  -   data
        data  data
        leftChild  N..
        rightChild  N..

___ insertNode(rootNode, nodeValue
    __ rootNode.data __ N..:
        rootNode.data  nodeValue
    ____ nodeValue < rootNode.data:
        __ rootNode.leftChild __ N..:
            rootNode.leftChild  BSTNode(nodeValue)
        ____
            insertNode(rootNode.leftChild, nodeValue)
    ____
        __ rootNode.rightChild __ N..:
            rootNode.rightChild  BSTNode(nodeValue)
        ____
            insertNode(rootNode.rightChild, nodeValue)
    r_ "The node has been successfully inserted"

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
        customQueue  queue.Queue()
        customQueue.enqueue(rootNode)
        w__ no.(customQueue.isEmpty()):
            root  customQueue.dequeue()
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


___ minValueNode(bstNode
    current  bstNode
    w__ (current.leftChild __ no. N..
        current  current.leftChild
    r_ current


___ deleteNode(rootNode, nodeValue
    __ rootNode __ N..:
        r_ rootNode
    __ nodeValue < rootNode.data:
        rootNode.leftChild  deleteNode(rootNode.leftChild, nodeValue)
    ____ nodeValue > rootNode.data:
        rootNode.rightChild  deleteNode(rootNode.rightChild, nodeValue)
    ____
        __ rootNode.leftChild __ N..:
            temp  rootNode.rightChild
            rootNode  N..
            r_ temp
        
        __ rootNode.rightChild __ N..:
            temp  rootNode.leftChild
            rootNode  N..
            r_ temp
        
        temp  minValueNode(rootNode.rightChild)
        rootNode.data  temp.data
        rootNode.rightChild  deleteNode(rootNode.rightChild, temp.data)
    r_ rootNode

___ deleteBST(rootNode
    rootNode.data  N..
    rootNode.leftChild  N..
    rootNode.rightChild  N..
    r_ "The BST has been successfully deleted"



newBST  BSTNode(N..)
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

