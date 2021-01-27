#   Created by Elshad Karimov on 05/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

class Node:
    ___ __init__(self, value=None
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    ___ __init__(self
        self.head = None
        self.tail = None

    
    ___ __iter__(self
        node = self.head
        while node:
            yield node
            node = node.next
    
    #  Creation of Doubly Linked List
    ___ createDLL(self, nodeValue
        node = Node(nodeValue)
        node.prev = None
        node.next = None
        self.head = node
        self.tail = node
        r_ "The DLL is created Successfully"
    
    
    
    #  Insertion Method in Doubly Linked List
    ___ insertNode(self, nodeValue, location
        __ self.head is None:
            print("The node cannot be inserted")
        ____
            newNode = Node(nodeValue)
            __ location == 0:
                newNode.prev = None
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            elif location == 1:
                newNode.next = None
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
            ____
                tempNode = self.head
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
        __ self.head is None:
            print("There is not any element to traverse")
        ____
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
    
    #  Reverse Traversal Method in Doubly Linked List
    ___ reverseTraversalDLL(self
        __ self.head is None:
            print("There is not any element to traverse")
        ____
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.prev

    # Search Method in Doubly Linked List
    ___ searchDLL(self, nodeValue
        __ self.head is None:
            r_ "There is not any element in the list"
        ____
            tempNode = self.head
            while tempNode:
                __ tempNode.value == nodeValue:
                    r_ tempNode.value
                tempNode = tempNode.next
            r_ "The node does not exist in this list"

    # Delete a node from Doubly Linked List
    ___ deleteNode(self,location
        __ self.head is None:
            print("There is not any element in DLL")
        ____
            __ location == 0:
                __ self.head == self.tail:
                    self.head = None
                    self.tail = None
                ____
                    self.head = self.head.next
                    self.head.prev = None
            elif location == 1:
                __ self.head == self.tail:
                    self.head = None
                    self.tail = None
                ____
                    self.tail = self.tail.prev
                    self.tail.next = None
            ____
                curNode = self.head
                index = 0
                while index < location - 1:
                    curNode = curNode.next
                    index += 1
                curNode.next = curNode.next.next
                curNode.next.prev = curNode
            print("The node has been successfully deleted")

    # Delete entire Doubly Linked List
    ___ deleteDLL(self
        __ self.head is None:
            print("There is not any node in DLL")
        ____
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None
            print("The DLL has been successfully deleted")
    


doubyLL = DoublyLinkedList()
doubyLL.createDLL(5)
doubyLL.insertNode(0,0)
doubyLL.insertNode(2,1)
doubyLL.insertNode(6,2)
print([node.value ___ node __ doubyLL])
doubyLL.deleteDLL()
print([node.value ___ node __ doubyLL])



