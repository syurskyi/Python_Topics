#   Created by Elshad Karimov on 04/06/2020.
#   Copyright © 2020 AppMillers. All rights reserved.
  
#   Create Stack with min method

c_ Node(
    ___  -   valueN.., next  N..
        value  value
        next  next
    
    ___ __str__(self
        string  st.(value)
        __ next:
            string + ',' + st.(next)
        r_ string

c_ Stack(
    ___  - (self
        top  N..
        minNode  N..
    
    ___ m..(self
        __ no. minNode:
            r_ N..
        r_ minNode.value
    
    ___ push  item
        __ minNode a__ (minNode.value < item
            minNode  Node(value  minNode.value, nextminNode)
        ____
            minNode  Node(value  item, nextminNode)
        top  Node(valueitem, nexttop)
    
    ___ pop(self
        __ no. top:
            r_ N..
        minNode  minNode.next
        item  top.value
        top  top.next
        r_ item

customStack  Stack()
customStack.push(5)
print(customStack.m..())
customStack.push(6)
print(customStack.m..())
customStack.push(3)
print(customStack.m..())
customStack.pop()
print(customStack.m..())

