#   Created by Elshad Karimov on 12/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

class Node:
    ___ __init__(self, value=None
        self.value = value
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    ___ __init__(self
        self.head = None
        self.tail = None

    
    ___ __iter__(self
        node = self.head
        while node:
            yield node
            node = node.next
            __ node == self.tail.next:
                break
    
    #  Creation of Circular Doubly Linked List
    ___ createCDLL(self, nodeValue
        newNode = Node(nodeValue)
        self.head = newNode
        self.tail = newNode
        newNode.prev = newNode
        newNode.next = newNode
        return "The CDLL is created successfully"


    # Insertion Method in Circular Doubly Linked List
    ___ insertCDLL(self, value, location
        __ self.head is None:
            return "The CDLL does not exist"
        ____
            newNode = Node(value)
            __ location == 0:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.head = newNode
                self.tail.next = newNode
            elif location == 1:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
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
            return "The node has been successfully inserted"

    # Traversal of Circular Doubly Linked List
    ___ traversalCDLL(self
        __ self.head is None:
            print("There is not any node for traversal")
        ____
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                __ tempNode == self.tail:
                    break
                tempNode = tempNode.next

    # Reverse traversal of Circular Doubly Linked List
    ___ reverseTraversalCDLL(self
        __ self.head is None:
            print("There is not any node for reverse traversal")
        ____
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                __ tempNode == self.head:
                    break
                tempNode = tempNode.prev
    
    # Search Circular Doubly Linked List
    ___ searchCDLL(self, nodeValue
        __ self.head is None:
            return "There is not any node in CDLL"
        ____
            tempNode = self.head
            while tempNode:
                __ tempNode.value == nodeValue:
                    return tempNode.value
                __ tempNode == self.tail:
                    return "The value does not exist in CDLL"
                tempNode = tempNode.next
    
    # Delete a node from Circular Doubly Linked List
    ___ deleteNode(self, location
        __ self.head is None:
            print("There is not any node to delete")
        ____
            __ location == 0:
                __ self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                ____
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
            elif location == 1:
                __ self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                ____
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
            ____
                curNode = self.head
                index = 0
                while index < location - 1:
                    curNode = curNode.next
                    index += 1
                curNode.next = curNode.next.next
                curNode.next.prev = curNode
            print("The node has been successfully deleted")
    
    # Delete entire Circular Doubly Linked List
    ___ deleteCDLL(self
        __ self.head is None:
            print("There is not any element to delete")
        ____
            self.tail.next = None
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None
            print("The CDLL has been successfully deleted")
    


circularDLL = CircularDoublyLinkedList()
circularDLL.createCDLL(5)
circularDLL.insertCDLL(0,0)
circularDLL.insertCDLL(1,1)
circularDLL.insertCDLL(2,2)
print([node.value for node in circularDLL])
circularDLL.deleteCDLL()
print([node.value for node in circularDLL])




    
