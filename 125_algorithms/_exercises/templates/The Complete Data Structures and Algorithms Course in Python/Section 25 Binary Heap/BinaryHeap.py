#   Created by Elshad Karimov 
#   Copyright © 2021 AppMillers. All rights reserved.

class Heap:
    ___ __init__(self, size
        self.customList = (size+1) * [None]
        self.heapSize = 0
        self.maxSize = size + 1

___ peekofHeap(rootNode
    __ not rootNode:
        return
    ____
        return rootNode.customList[1]

___ sizeofHeap(rootNode
    __ not rootNode:
        return
    ____
        return rootNode.heapSize

___ levelOrderTraversal(rootNode
    __ not rootNode:
        return
    ____
        for i in range(1, rootNode.heapSize+1
            print(rootNode.customList[i])

___ heapifyTreeInsert(rootNode, index, heapType
    parentIndex = int(index/2)
    __ index <= 1:
        return
    __ heapType == "Min":
        __ rootNode.customList[index] < rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
        heapifyTreeInsert(rootNode, parentIndex, heapType)
    elif heapType == "Max":
        __ rootNode.customList[index] > rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
        heapifyTreeInsert(rootNode, parentIndex, heapType)

___ inserNode(rootNode, nodeValue, heapType
    __ rootNode.heapSize + 1 == rootNode.maxSize:
        return "The Binary Heap is Full"
    rootNode.customList[rootNode.heapSize + 1] = nodeValue
    rootNode.heapSize += 1
    heapifyTreeInsert(rootNode, rootNode.heapSize, heapType)
    return "The value has been successfully inserted"

___ heapifyTreeExtract(rootNode, index, heapType
    leftIndex = index * 2
    rightIndex = index * 2 + 1
    swapChild = 0

    __ rootNode.heapSize < leftIndex:
        return
    elif rootNode.heapSize == leftIndex:
        __ heapType == "Min":
            __ rootNode.customList[index] > rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return
        ____
            __ rootNode.customList[index] < rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return

    ____
        __ heapType == "Min":
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
    __ rootNode.heapSize == 0:
        return
    ____
        extractedNode = rootNode.customList[1]
        rootNode.customList[1] = rootNode.customList[rootNode.heapSize]
        rootNode.customList[rootNode.heapSize] = None
        rootNode.heapSize -= 1
        heapifyTreeExtract(rootNode, 1, heapType)
        return extractedNode

___ deleteEntireBP(rootNode
    rootNode.customList = None








newHeap = Heap(5)
inserNode(newHeap, 4, "Max")
inserNode(newHeap, 5, "Max")
inserNode(newHeap, 2, "Max")
inserNode(newHeap, 1, "Max")
deleteEntireBP(newHeap)
levelOrderTraversal(newHeap)


