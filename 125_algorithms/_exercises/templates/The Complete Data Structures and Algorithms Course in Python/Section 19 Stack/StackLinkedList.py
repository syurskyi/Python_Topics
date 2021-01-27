#   Created by Elshad Karimov on 23/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

class Node:
    ___ __init__(self, value = None
        self.value = value
        self.next = None

class LinkedList:
    ___ __init__(self
        self.head = None
    
    ___ __iter__(self
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next

class Stack:
    ___ __init__(self
        self.LinkedList = LinkedList()
    
    ___ __str__(self
        values = [str(x.value) ___ x __ self.LinkedList]
        r_ '\n'.join(values)
    
    ___ isEmpty(self
        __ self.LinkedList.head == None:
            r_ True
        ____
            r_ False

    ___ push(self, value
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node
    
    ___ pop(self
        __ self.isEmpty(
            r_ "There is not any element in the stack"
        ____
            nodeValue = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            r_ nodeValue
    
    ___ peek(self
        __ self.isEmpty(
            r_ "There is not any element in the stack"
        ____
            nodeValue = self.LinkedList.head.value
            r_ nodeValue
    
    ___ delete(self
        self.LinkedList.head = None
    



customStack = Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)

print(customStack.peek())

