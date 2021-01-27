#   Created by Elshad Karimov on 01/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

c_ Node:
    ___  -   value=N..
        value = value
        next = N..

c_ CircularSinglyLinkedList:
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
            

    #  Creation of circular singly linked list
    ___ createCSLL  nodeValue
        node = Node(nodeValue)
        node.next = node
        head = node
        tail = node
        r_ "The CSLL has been created"
    
    #  Insertion of a node in circular singly linked list

    ___ insertCSLL  value, location
        __ head __ N..:
            r_ "The head reference is None"
        ____
            newNode = Node(value)
            __ location __ 0:
                newNode.next = head
                head = newNode
                tail.next = newNode
            elif location __ 1:
                newNode.next = tail.next
                tail.next = newNode
                tail = newNode
            ____
                tempNode = head
                index = 0
                w__ index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
            r_ "The node has been successfully inserted"
    
    # Traversal of a node in circular singly linked list
    ___ traversalCSLL(self
        __ head __ N..:
            print("There is not any element for traversal")
        ____
            tempNode = head
            w__ tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
                __ tempNode __ tail.next:
                    break
    
    # Searching for a node in circular singly linked list
    ___ searchCSLL  nodeValue
        __ head __ N..:
            r_ "There is not any node in this CSLL"
        ____
            tempNode = head
            w__ tempNode:
                __ tempNode.value __ nodeValue:
                    r_ tempNode.value
                tempNode = tempNode.next
                __ tempNode __ tail.next:
                    r_ "The node does not exist in this CSLL"

    # Delete  a node from circular singly linked list
    ___ deleteNode  location
        __ head __ N..:
            print("There is not any node in CSLL")
        ____
            __ location __ 0:
                __ head __ tail:
                    head.next = N..
                    head = N..
                    tail = N..
                ____
                    head = head.next
                    tail.next = head
            elif location __ 1:
                __ head __ tail:
                    head.next = N..
                    head = N..
                    tail = N..
                ____
                    node = head
                    w__ node __ not N..:
                        __ node.next __ tail:
                            break
                        node = node.next
                    node.next = head
                    tail = node
            ____
                tempNode = head
                index = 0
                w__ index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next
    
    # Delete entire circular sinlgy linked list
    ___ deleteEntireCSLL(self
        head = N..
        tail.next = N..
        tail = N..



circularSLL = CircularSinglyLinkedList()
circularSLL.createCSLL(0)
circularSLL.insertCSLL(1,1)
circularSLL.insertCSLL(2,1)
circularSLL.insertCSLL(3,1)

print([node.value ___ node __ circularSLL])
circularSLL.deleteEntireCSLL()
print([node.value ___ node __ circularSLL])












