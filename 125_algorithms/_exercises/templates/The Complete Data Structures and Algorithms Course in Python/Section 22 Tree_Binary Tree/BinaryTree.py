#   Created by Elshad Karimov 
#   Copyright © 2020 AppMillers. All rights reserved.

_____ QueueLinkedList as queue

c_ TreeNode:
    ___  -   data
        data = data
        leftChild = N..
        rightChild = N..

newBT = TreeNode("Drinks")
leftChild = TreeNode("Hot")
tea = TreeNode("Tea")
coffee = TreeNode("Coffee")
leftChild.leftChild = tea
leftChild.rightChild = coffee
rightChild = TreeNode("Cold")
newBT.leftChild = leftChild
newBT.rightChild = rightChild

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
            __ (root.value.leftChild __ no. N..
                customQueue.enqueue(root.value.leftChild)
            
            __ (root.value.rightChild __ no. N..
                customQueue.enqueue(root.value.rightChild)

___ searchBT(rootNode, nodeValue
    __ no. rootNode:
        r_ "The BT does not exist"
    ____
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        w__ no.(customQueue.isEmpty()):
            root = customQueue.dequeue()
            __ root.value.data __ nodeValue:
                r_ "Success"
            __ (root.value.leftChild __ no. N..
                customQueue.enqueue(root.value.leftChild)
            
            __ (root.value.rightChild __ no. N..
                customQueue.enqueue(root.value.rightChild)
        r_ "Not found"

___ insertNodeBT(rootNode, newNode
    __ no. rootNode:
        rootNode = newNode
    ____
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        w__ no.(customQueue.isEmpty()):
            root = customQueue.dequeue()
            __ root.value.leftChild __ no. N..:
                customQueue.enqueue(root.value.leftChild)
            ____
                root.value.leftChild = newNode
                r_ "Successfully Inserted"
            __ root.value.rightChild __ no. N..:
                customQueue.enqueue(root.value.rightChild)
            ____
                root.value.rightChild = newNode
                r_ "Successfully Inserted"

___ getDeepestNode(rootNode
    __ no. rootNode:
        r_
    ____
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        w__ no.(customQueue.isEmpty()):
            root = customQueue.dequeue()
            __ (root.value.leftChild __ no. N..
                customQueue.enqueue(root.value.leftChild)
            
            __ (root.value.rightChild __ no. N..
                customQueue.enqueue(root.value.rightChild)
        deepestNode = root.value
        r_ deepestNode

___ deleteDeepestNode(rootNode, dNode
    __ no. rootNode:
        r_
    ____
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        w__ no.(customQueue.isEmpty()):
            root = customQueue.dequeue()
            __ root.value __ dNode:
                root.value = N..
                r_
            __ root.value.rightChild:
                __ root.value.rightChild __ dNode:
                    root.value.rightChild = N..
                    r_
                ____
                    customQueue.enqueue(root.value.rightChild)
            __ root.value.leftChild:
                __ root.value.leftChild __ dNode:
                    root.value.leftChild = N..
                    r_
                ____
                    customQueue.enqueue(root.value.leftChild)

___ deleteNodeBT(rootNode, node
    __ no. rootNode:
        r_ "The BT does not exist"
    ____
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        w__ no.(customQueue.isEmpty()):
            root = customQueue.dequeue()
            __ root.value.data __ node:
                dNode = getDeepestNode(rootNode)
                root.value.data = dNode.data
                deleteDeepestNode(rootNode, dNode)
                r_ "The node has been successfully deleted"
            __ (root.value.leftChild __ no. N..
                customQueue.enqueue(root.value.leftChild)
            
            __ (root.value.rightChild __ no. N..
                customQueue.enqueue(root.value.rightChild)
        r_ "Failed to delete"

___ deleteBT(rootNode
    rootNode.data = N..
    rootNode.leftChild = N..
    rootNode.rightChild = N..
    r_ "The BT has been successfully deleted"

inOrderTraversal(newBT)

        
            





