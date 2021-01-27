#   Created by Elshad Karimov 
#   Copyright © 2021 AppMillers. All rights reserved.

c_ Heap:
    ___  -   size
        customList = (size+1) * [N..]
        heapSize = 0
        maxSize = size + 1

___ peekofHeap(rootNode
    __ not rootNode:
        r_
    ____
        r_ rootNode.customList[1]

___ sizeofHeap(rootNode
    __ not rootNode:
        r_
    ____
        r_ rootNode.heapSize

___ levelOrderTraversal(rootNode
    __ not rootNode:
        r_
    ____
        ___ i __ ra__(1, rootNode.heapSize+1
            print(rootNode.customList[i])

___ heapifyTreeInsert(rootNode, index, heapType
    parentIndex = in.(index/2)
    __ index <= 1:
        r_
    __ heapType __ "Min":
        __ rootNode.customList[index] < rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
        heapifyTreeInsert(rootNode, parentIndex, heapType)
    ____ heapType __ "Max":
        __ rootNode.customList[index] > rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
        heapifyTreeInsert(rootNode, parentIndex, heapType)

___ inserNode(rootNode, nodeValue, heapType
    __ rootNode.heapSize + 1 __ rootNode.maxSize:
        r_ "The Binary Heap is Full"
    rootNode.customList[rootNode.heapSize + 1] = nodeValue
    rootNode.heapSize += 1
    heapifyTreeInsert(rootNode, rootNode.heapSize, heapType)
    r_ "The value has been successfully inserted"

___ heapifyTreeExtract(rootNode, index, heapType
    leftIndex = index * 2
    rightIndex = index * 2 + 1
    swapChild = 0

    __ rootNode.heapSize < leftIndex:
        r_
    ____ rootNode.heapSize __ leftIndex:
        __ heapType __ "Min":
            __ rootNode.customList[index] > rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            r_
        ____
            __ rootNode.customList[index] < rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            r_

    ____
        __ heapType __ "Min":
            __ rootNode.customList[leftIndex] < rootNode.customList[rightIndex]:
                swapChild = leftIndex
            ____
                swapChild = rightIndex
            __ rootNode.customList[index] > rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp
        ____
            __ rootNode.customList[leftIndex] > rootNode.customList[rightIndex]:
                swapChild = leftIndex
            ____
                swapChild = rightIndex
            __ rootNode.customList[index] < rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp
    heapifyTreeExtract(rootNode, swapChild, heapType)

___ extractNode(rootNode, heapType
    __ rootNode.heapSize __ 0:
        r_
    ____
        extractedNode = rootNode.customList[1]
        rootNode.customList[1] = rootNode.customList[rootNode.heapSize]
        rootNode.customList[rootNode.heapSize] = N..
        rootNode.heapSize -= 1
        heapifyTreeExtract(rootNode, 1, heapType)
        r_ extractedNode

___ deleteEntireBP(rootNode
    rootNode.customList = N..








newHeap = Heap(5)
inserNode(newHeap, 4, "Max")
inserNode(newHeap, 5, "Max")
inserNode(newHeap, 2, "Max")
inserNode(newHeap, 1, "Max")
deleteEntireBP(newHeap)
levelOrderTraversal(newHeap)


