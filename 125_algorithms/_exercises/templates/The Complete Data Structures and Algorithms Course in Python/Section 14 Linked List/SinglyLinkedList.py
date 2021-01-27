#   Created by Elshad Karimov on 27/04/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

class Node:
    ___ __init__(self, value=None
        self.value = value
        self.next = None

class SLinkedList:
    ___ __init__(self
        self.head = None
        self.tail = None
    ___ __iter__(self
        node = self.head
        while node:
            yield node
            node = node.next
    # insert in Linked List
    ___ insertSLL(self, value, location
        newNode = Node(value)
        __ self.head is None:
            self.head = newNode
            self.tail = newNode
        ____
            __ location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == 1:
                newNode.next = None
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

    # Traverse Singly Linked List
    ___ traverseSLL(self
        __ self.head is None:
            print("The Singly Linked List does not exist")
        ____
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next
    # Search for a node in Singly Linked List
    ___ searchSLL(self, nodeValue
        __ self.head is None:
           return "The list does not exist"
        ____
            node = self.head
            while node is not None:
                __ node.value == nodeValue:
                    return node.value
                node = node.next
            return "The value does not exist in this list"

    #  Delete a node from Singly Linked List
    ___ deleteNode(self, location
        __ self.head is None:
            print("The SLL does not exist")
        ____
            __ location == 0:
                __ self.head == self.tail:
                    self.head = None
                    self.tail = None
                ____
                    self.head = self.head.next
            elif location == 1:
                __ self.head == self.tail:
                    self.head = None
                    self.tail = None
                ____
                    node = self.head
                    while node is not None:
                        __ node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            ____
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next
    # Delete entire SLL
    ___ deleteEntireSLL(self
        __ self.head is None:
            print("The SLL does not exist")
        ____
            self.head = None
            self.tail = None


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






