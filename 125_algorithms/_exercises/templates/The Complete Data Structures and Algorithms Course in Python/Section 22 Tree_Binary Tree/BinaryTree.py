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
            __ (root.value.leftChild is not None
                customQueue.enqueue(root.value.leftChild)
            
            __ (root.value.rightChild is not None
                customQueue.enqueue(root.value.rightChild)

___ searchBT(rootNode, nodeValue
    __ not rootNode:
        return "The BT does not exist"
    ____
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            __ root.value.data == nodeValue:
                return "Success"
            __ (root.value.leftChild is not None
                customQueue.enqueue(root.value.leftChild)
            
            __ (root.value.rightChild is not None
                customQueue.enqueue(root.value.rightChild)
        return "Not found"

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
                return "Successfully Inserted"
            __ root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
            ____
                root.value.rightChild = newNode
                return "Successfully Inserted"

___ getDeepestNode(rootNode
    __ not rootNode:
        return
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
        return deepestNode

___ deleteDeepestNode(rootNode, dNode
    __ not rootNode:
        return
    ____
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            __ root.value is dNode:
                root.value = None
                return
            __ root.value.rightChild:
                __ root.value.rightChild is dNode:
                    root.value.rightChild = None
                    return
                ____
                    customQueue.enqueue(root.value.rightChild)
            __ root.value.leftChild:
                __ root.value.leftChild is dNode:
                    root.value.leftChild = None
                    return
                ____
                    customQueue.enqueue(root.value.leftChild)

___ deleteNodeBT(rootNode, node
    __ not rootNode:
        return "The BT does not exist"
    ____
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            __ root.value.data == node:
                dNode = getDeepestNode(rootNode)
                root.value.data = dNode.data
                deleteDeepestNode(rootNode, dNode)
                return "The node has been successfully deleted"
            __ (root.value.leftChild is not None
                customQueue.enqueue(root.value.leftChild)
            
            __ (root.value.rightChild is not None
                customQueue.enqueue(root.value.rightChild)
        return "Failed to delete"

___ deleteBT(rootNode
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "The BT has been successfully deleted" 

inOrderTraversal(newBT)

        
            





