#   Created by Elshad Karimov on 30/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.


class Node:
    ___ __init__(self, value=None
        self.value = value
        self.next = None
    
    ___ __str__(self
        return str(self.value)

class LinkedList:
    ___ __init__(self
        self.head = None
        self.tail = None
    
    

class Queue:
    ___ __init__(self
        self.linkedList = LinkedList()
    
    ___ __str__(self
        values = [str(x) for x in self.linkedList]
        return ' '.join(values)
    
    ___ enqueue(self, value
        newNode = Node(value)
        __ self.linkedList.head == None:
            self.linkedList.head = newNode
            self.linkedList.tail = newNode
        ____
            self.linkedList.tail.next = newNode
            self.linkedList.tail = newNode
    
    ___ isEmpty(self
        __ self.linkedList.head == None:
            return True
        ____
            return False
    
    ___ dequeue(self
        __ self.isEmpty(
            return "There is not any node in the Queue"
        ____
            tempNode = self.linkedList.head
            __ self.linkedList.head == self.linkedList.tail:
                self.linkedList.head = None
                self.linkedList.tail = None
            ____
                self.linkedList.head = self.linkedList.head.next
            return tempNode
    
    ___ peek(self
        __ self.isEmpty(
            return "There is not any node in the Queue"
        ____
            return self.linkedList.head
    
    ___ delete(self
        self.linkedList.head = None
        self.linkedList.tail = None




# custQueue = Queue()
# custQueue.enqueue(1)
# custQueue.enqueue(2)
# custQueue.enqueue(3)
# print(custQueue)
# print(custQueue.peek())
# print(custQueue)