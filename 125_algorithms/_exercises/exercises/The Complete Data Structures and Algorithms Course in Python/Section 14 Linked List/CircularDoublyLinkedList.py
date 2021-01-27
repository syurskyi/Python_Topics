#   Created by Elshad Karimov on 12/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

c_ Node:
    ___  -   value=N..
        value = value
        next = N..
        prev = N..

c_ CircularDoublyLinkedList:
    ___  - (self
        head = N..
        tail = N..

    
    ___ __iter__(self
        node = head
        w__ node:
            yield node
            node = node.next
            __ node __ tail.next:
                break
    
    #  Creation of Circular Doubly Linked List
    ___ createCDLL  nodeValue
        newNode = Node(nodeValue)
        head = newNode
        tail = newNode
        newNode.prev = newNode
        newNode.next = newNode
        r_ "The CDLL is created successfully"


    # Insertion Method in Circular Doubly Linked List
    ___ insertCDLL  value, location
        __ head __ N..:
            r_ "The CDLL does not exist"
        ____
            newNode = Node(value)
            __ location __ 0:
                newNode.next = head
                newNode.prev = tail
                head.prev = newNode
                head = newNode
                tail.next = newNode
            ____ location __ 1:
                newNode.next = head
                newNode.prev = tail
                head.prev = newNode
                tail.next = newNode
                tail = newNode
            ____
                tempNode = head
                index = 0
                w__ index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.next.prev = newNode
                tempNode.next = newNode
            r_ "The node has been successfully inserted"

    # Traversal of Circular Doubly Linked List
    ___ traversalCDLL(self
        __ head __ N..:
            print("There is not any node for traversal")
        ____
            tempNode = head
            w__ tempNode:
                print(tempNode.value)
                __ tempNode __ tail:
                    break
                tempNode = tempNode.next

    # Reverse traversal of Circular Doubly Linked List
    ___ reverseTraversalCDLL(self
        __ head __ N..:
            print("There is not any node for reverse traversal")
        ____
            tempNode = tail
            w__ tempNode:
                print(tempNode.value)
                __ tempNode __ head:
                    break
                tempNode = tempNode.prev
    
    # Search Circular Doubly Linked List
    ___ searchCDLL  nodeValue
        __ head __ N..:
            r_ "There is not any node in CDLL"
        ____
            tempNode = head
            w__ tempNode:
                __ tempNode.value __ nodeValue:
                    r_ tempNode.value
                __ tempNode __ tail:
                    r_ "The value does not exist in CDLL"
                tempNode = tempNode.next
    
    # Delete a node from Circular Doubly Linked List
    ___ deleteNode  location
        __ head __ N..:
            print("There is not any node to delete")
        ____
            __ location __ 0:
                __ head __ tail:
                    head.prev = N..
                    head.next = N..
                    head = N..
                    tail = N..
                ____
                    head = head.next
                    head.prev = tail
                    tail.next = head
            ____ location __ 1:
                __ head __ tail:
                    head.prev = N..
                    head.next = N..
                    head = N..
                    tail = N..
                ____
                    tail = tail.prev
                    tail.next = head
                    head.prev = tail
            ____
                curNode = head
                index = 0
                w__ index < location - 1:
                    curNode = curNode.next
                    index += 1
                curNode.next = curNode.next.next
                curNode.next.prev = curNode
            print("The node has been successfully deleted")
    
    # Delete entire Circular Doubly Linked List
    ___ deleteCDLL(self
        __ head __ N..:
            print("There is not any element to delete")
        ____
            tail.next = N..
            tempNode = head
            w__ tempNode:
                tempNode.prev = N..
                tempNode = tempNode.next
            head = N..
            tail = N..
            print("The CDLL has been successfully deleted")
    


circularDLL = CircularDoublyLinkedList()
circularDLL.createCDLL(5)
circularDLL.insertCDLL(0,0)
circularDLL.insertCDLL(1,1)
circularDLL.insertCDLL(2,2)
print([node.value ___ node __ circularDLL])
circularDLL.deleteCDLL()
print([node.value ___ node __ circularDLL])




    
