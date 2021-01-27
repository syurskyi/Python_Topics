#   Created by Elshad Karimov on 23/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

c_ Node:
    ___  -   value = N..
        value = value
        next = N..

c_ LinkedList:
    ___  - (self
        head = N..
    
    ___ __iter__(self
        curNode = head
        while curNode:
            yield curNode
            curNode = curNode.next

c_ Stack:
    ___  - (self
        LinkedList = LinkedList()
    
    ___ __str__(self
        values = [str(x.value) ___ x __ LinkedList]
        r_ '\n'.join(values)
    
    ___ isEmpty(self
        __ LinkedList.head __ N..:
            r_ T..
        ____
            r_ F..

    ___ push  value
        node = Node(value)
        node.next = LinkedList.head
        LinkedList.head = node
    
    ___ pop(self
        __ isEmpty(
            r_ "There is not any element in the stack"
        ____
            nodeValue = LinkedList.head.value
            LinkedList.head = LinkedList.head.next
            r_ nodeValue
    
    ___ peek(self
        __ isEmpty(
            r_ "There is not any element in the stack"
        ____
            nodeValue = LinkedList.head.value
            r_ nodeValue
    
    ___ delete(self
        LinkedList.head = N..
    



customStack = Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)

print(customStack.peek())

