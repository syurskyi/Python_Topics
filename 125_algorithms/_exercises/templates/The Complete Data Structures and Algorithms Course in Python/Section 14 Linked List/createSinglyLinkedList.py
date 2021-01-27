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
    
    ___ traverseList(self
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
            print("The Singly Linked List does not exist")
        ____
            node = self.head
            while node is not None:
                __ node.value == nodeValue:
                    r_ node.value
                node = node.next
            r_ "The node does not exist in this SLL"
    # Delete a node from Singly Linked List
    ___ deleteNode(self, location
        __ self.head is None:
            r_ "The Singly Linked List does not exist"
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
                while index < location-1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next
    # Delete entire SLL
    ___ deleteEntireSLL(self
        __ self.head is None:
            print("SLL does not exist")
        ____
            self.head = None
            self.tail = None

singlyLinkedList = SLinkedList()
singlyLinkedList.insertSLL(44,6)
print([node.value ___ node __ singlyLinkedList])

# node1 = Node(1)
# node2 = Node(2)

# singlyLinkedList.head = node1
# singlyLinkedList.head.next = node2
# singlyLinkedList.tail = node2

singlyLinkedList.insertSLL(3,1)
singlyLinkedList.insertSLL(4,1)
print([node.value ___ node __ singlyLinkedList])
singlyLinkedList.insertSLL(5,3)
print([node.value ___ node __ singlyLinkedList])


