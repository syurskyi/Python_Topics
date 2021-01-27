#   Created by Elshad Karimov 
#   Copyright © 2020 AppMillers. All rights reserved.

import QueueLinkedList as queue

class TreeNode:
    ___ __init__(self, data
        self.data = data
        self.leftChild = None
        self.rightChild = None

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
    __ not rootNode:
        r_
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

___ inOrderTraversal(rootNode
    __ not rootNode:
        r_
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

___ postOrderTraversal(rootNode
    __ not rootNode:
        r_
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

___ levelOrderTraversal(rootNode
    __ not rootNode:
        r_
    ____
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            __ (root.value.leftChild is not None
                customQueue.enqueue(root.value.leftChild)
            
            __ (root.value.rightChild is not None
                customQueue.enqueue(root.value.rightChild)

___ searchBT(rootNode, nodeValue
    __ not rootNode:
        r_ "The BT does not exist"
    ____
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            __ root.value.data == nodeValue:
                r_ "Success"
            __ (root.value.leftChild is not None
                customQueue.enqueue(root.value.leftChild)
            
            __ (root.value.rightChild is not None
                customQueue.enqueue(root.value.rightChild)
        r_ "Not found"

___ insertNodeBT(rootNode, newNode
    __ not rootNode:
        rootNode = newNode
    ____
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            __ root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            ____
                root.value.leftChild = newNode
                r_ "Successfully Inserted"
            __ root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
            ____
                root.value.rightChild = newNode
                r_ "Successfully Inserted"

___ getDeepestNode(rootNode
    __ not rootNode:
        r_
    ____
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            __ (root.value.leftChild is not None
                customQueue.enqueue(root.value.leftChild)
            
            __ (root.value.rightChild is not None
                customQueue.enqueue(root.value.rightChild)
        deepestNode = root.value
        r_ deepestNode

___ deleteDeepestNode(rootNode, dNode
    __ not rootNode:
        r_
    ____
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            __ root.value is dNode:
                root.value = None
                r_
            __ root.value.rightChild:
                __ root.value.rightChild is dNode:
                    root.value.rightChild = None
                    r_
                ____
                    customQueue.enqueue(root.value.rightChild)
            __ root.value.leftChild:
                __ root.value.leftChild is dNode:
                    root.value.leftChild = None
                    r_
                ____
                    customQueue.enqueue(root.value.leftChild)

___ deleteNodeBT(rootNode, node
    __ not rootNode:
        r_ "The BT does not exist"
    ____
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            __ root.value.data == node:
                dNode = getDeepestNode(rootNode)
                root.value.data = dNode.data
                deleteDeepestNode(rootNode, dNode)
                r_ "The node has been successfully deleted"
            __ (root.value.leftChild is not None
                customQueue.enqueue(root.value.leftChild)
            
            __ (root.value.rightChild is not None
                customQueue.enqueue(root.value.rightChild)
        r_ "Failed to delete"

___ deleteBT(rootNode
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    r_ "The BT has been successfully deleted"

inOrderTraversal(newBT)

        
            





