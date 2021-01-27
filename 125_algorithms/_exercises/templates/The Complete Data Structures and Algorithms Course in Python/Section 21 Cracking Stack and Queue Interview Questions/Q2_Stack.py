#   Created by Elshad Karimov on 04/06/2020.
#   Copyright © 2020 AppMillers. All rights reserved.
  
#   Create Stack with min method

c_ Node(
    ___  -   value=N.., next = N..
        value = value
        next = next
    
    ___ __str__(self
        string = st.(value)
        __ next:
            string += ',' + st.(next)
        r_ string

c_ Stack(
    ___  - (self
        top = N..
        minNode = N..
    
    ___ min(self
        __ not minNode:
            r_ N..
        r_ minNode.value
    
    ___ push  item
        __ minNode a__ (minNode.value < item
            minNode = Node(value = minNode.value, next=minNode)
        ____
            minNode = Node(value = item, next=minNode)
        top = Node(value=item, next=top)
    
    ___ pop(self
        __ not top:
            r_ N..
        minNode = minNode.next
        item = top.value
        top = top.next
        r_ item

customStack = Stack()
customStack.push(5)
print(customStack.min())
customStack.push(6)
print(customStack.min())
customStack.push(3)
print(customStack.min())
customStack.pop()
print(customStack.min())

