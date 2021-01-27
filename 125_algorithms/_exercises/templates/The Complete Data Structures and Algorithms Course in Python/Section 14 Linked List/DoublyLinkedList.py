#   Created by Elshad Karimov on 05/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

c_ Node:
    ___  -   value=N..
        value = value
        next = N..
        prev = N..

c_ DoublyLinkedList:
    ___  - (self
        head = N..
        tail = N..

    
    ___ __iter__(self
        node = head
        while node:
            yield node
            node = node.next
    
    #  Creation of Doubly Linked List
    ___ createDLL  nodeValue
        node = Node(nodeValue)
        node.prev = N..
        node.next = N..
        head = node
        tail = node
        r_ "The DLL is created Successfully"
    
    
    
    #  Insertion Method in Doubly Linked List
    ___ insertNode  nodeValue, location
        __ head __ N..:
            print("The node cannot be inserted")
        ____
            newNode = Node(nodeValue)
            __ location __ 0:
                newNode.prev = N..
                newNode.next = head
                head.prev = newNode
                head = newNode
            elif location __ 1:
                newNode.next = N..
                newNode.prev = tail
                tail.next = newNode
                tail = newNode
            ____
                tempNode = head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.next.prev = newNode
                tempNode.next = newNode
    
    #  Traversal Method in Doubly Linked List
    ___ traverseDLL(self
        __ head __ N..:
            print("There is not any element to traverse")
        ____
            tempNode = head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
    
    #  Reverse Traversal Method in Doubly Linked List
    ___ reverseTraversalDLL(self
        __ head __ N..:
            print("There is not any element to traverse")
        ____
            tempNode = tail
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.prev

    # Search Method in Doubly Linked List
    ___ searchDLL  nodeValue
        __ head __ N..:
            r_ "There is not any element in the list"
        ____
            tempNode = head
            while tempNode:
                __ tempNode.value __ nodeValue:
                    r_ tempNode.value
                tempNode = tempNode.next
            r_ "The node does not exist in this list"

    # Delete a node from Doubly Linked List
    ___ deleteNode location
        __ head __ N..:
            print("There is not any element in DLL")
        ____
            __ location __ 0:
                __ head __ tail:
                    head = N..
                    tail = N..
                ____
                    head = head.next
                    head.prev = N..
            elif location __ 1:
                __ head __ tail:
                    head = N..
                    tail = N..
                ____
                    tail = tail.prev
                    tail.next = N..
            ____
                curNode = head
                index = 0
                while index < location - 1:
                    curNode = curNode.next
                    index += 1
                curNode.next = curNode.next.next
                curNode.next.prev = curNode
            print("The node has been successfully deleted")

    # Delete entire Doubly Linked List
    ___ deleteDLL(self
        __ head __ N..:
            print("There is not any node in DLL")
        ____
            tempNode = head
            while tempNode:
                tempNode.prev = N..
                tempNode = tempNode.next
            head = N..
            tail = N..
            print("The DLL has been successfully deleted")
    


doubyLL = DoublyLinkedList()
doubyLL.createDLL(5)
doubyLL.insertNode(0,0)
doubyLL.insertNode(2,1)
doubyLL.insertNode(6,2)
print([node.value ___ node __ doubyLL])
doubyLL.deleteDLL()
print([node.value ___ node __ doubyLL])



