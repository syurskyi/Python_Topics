#   Created by Elshad Karimov on 27/04/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

c_ Node:
    ___  -   value=N..
        value = value
        next = N..

c_ SLinkedList:
    ___  - (self
        head = N..
        tail = N..
    ___ __iter__(self
        node = head
        w__ node:
            yield node
            node = node.next
    # insert in Linked List
    ___ insertSLL  value, location
        newNode = Node(value)
        __ head __ N..:
            head = newNode
            tail = newNode
        ____
            __ location __ 0:
                newNode.next = head
                head = newNode
            elif location __ 1:
                newNode.next = N..
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

    # Traverse Singly Linked List
    ___ traverseSLL(self
        __ head __ N..:
            print("The Singly Linked List does not exist")
        ____
            node = head
            w__ node __ not N..:
                print(node.value)
                node = node.next
    # Search for a node in Singly Linked List
    ___ searchSLL  nodeValue
        __ head __ N..:
           r_ "The list does not exist"
        ____
            node = head
            w__ node __ not N..:
                __ node.value __ nodeValue:
                    r_ node.value
                node = node.next
            r_ "The value does not exist in this list"

    #  Delete a node from Singly Linked List
    ___ deleteNode  location
        __ head __ N..:
            print("The SLL does not exist")
        ____
            __ location __ 0:
                __ head __ tail:
                    head = N..
                    tail = N..
                ____
                    head = head.next
            elif location __ 1:
                __ head __ tail:
                    head = N..
                    tail = N..
                ____
                    node = head
                    w__ node __ not N..:
                        __ node.next __ tail:
                            break
                        node = node.next
                    node.next = N..
                    tail = node
            ____
                tempNode = head
                index = 0
                w__ index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next
    # Delete entire SLL
    ___ deleteEntireSLL(self
        __ head __ N..:
            print("The SLL does not exist")
        ____
            head = N..
            tail = N..


singlyLinkedList = SLinkedList()
singlyLinkedList.insertSLL(1, 1)
singlyLinkedList.insertSLL(2, 1)
singlyLinkedList.insertSLL(3, 1)
singlyLinkedList.insertSLL(4, 1)
singlyLinkedList.insertSLL(0, 0)
singlyLinkedList.insertSLL(0, 4)


# print([node.value for node in singlyLinkedList]) 
# singlyLinkedList.deleteEntireSLL()
# print([node.value for node in singlyLinkedList]) 






