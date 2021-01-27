#   Created by Elshad Karimov on 01/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

class Node:
    ___ __init__(self, value=None
        self.value = value
        self.next = None

class CircularSinglyLinkedList:
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
            

    #  Creation of circular singly linked list
    ___ createCSLL(self, nodeValue
        node = Node(nodeValue)
        node.next = node
        self.head = node
        self.tail = node
        return "The CSLL has been created"
    
    #  Insertion of a node in circular singly linked list

    ___ insertCSLL(self, value, location
        __ self.head is None:
            return "The head reference is None"
        ____
            newNode = Node(value)
            __ location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            elif location == 1:
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode
            ____
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
            return "The node has been successfully inserted"
    
    # Traversal of a node in circular singly linked list
    ___ traversalCSLL(self
        __ self.head is None:
            print("There is not any element for traversal")
        ____
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
                __ tempNode == self.tail.next:
                    break
    
    # Searching for a node in circular singly linked list
    ___ searchCSLL(self, nodeValue
        __ self.head is None:
            return "There is not any node in this CSLL"
        ____
            tempNode = self.head
            while tempNode:
                __ tempNode.value == nodeValue:
                    return tempNode.value
                tempNode = tempNode.next
                __ tempNode == self.tail.next:
                    return "The node does not exist in this CSLL"

    # Delete  a node from circular singly linked list
    ___ deleteNode(self, location
        __ self.head is None:
            print("There is not any node in CSLL")
        ____
            __ location == 0:
                __ self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                ____
                    self.head = self.head.next
                    self.tail.next = self.head
            elif location == 1:
                __ self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                ____
                    node = self.head
                    while node is not None:
                        __ node.next == self.tail:
                            break
                        node = node.next
                    node.next = self.head
                    self.tail = node
            ____
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next
    
    # Delete entire circular sinlgy linked list
    ___ deleteEntireCSLL(self
        self.head = None
        self.tail.next = None
        self.tail = None



circularSLL = CircularSinglyLinkedList()
circularSLL.createCSLL(0)
circularSLL.insertCSLL(1,1)
circularSLL.insertCSLL(2,1)
circularSLL.insertCSLL(3,1)

print([node.value for node in circularSLL]) 
circularSLL.deleteEntireCSLL()
print([node.value for node in circularSLL]) 












