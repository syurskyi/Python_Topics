#   Created by Elshad Karimov on 19/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

# Question 5 - Intersection

____ LinkedList _____ LinkedList, Node

___ intersection(llA, llB
    __ llA.tail __ no. llB.tail:
        r_ F..
    
    lenA  le_(llA)
    lenB  le_(llB)

    shorter  llA __ lenA < lenB else llB
    longer  llB __ lenA < lenB else llA

    diff  le_(longer) - le_(shorter)
    longerNode  longer.head
    shorterNode  shorter.head

    ___ i __ ra__(diff
        longerNode  longerNode.next
    
    w__ shorterNode __ no. longerNode:
        shorterNode  shorterNode.next
        longerNode  longerNode.next
    
    r_ longerNode


# Helper addition method
___ addSameNode(llA, llB, value
    tempNode  Node(value)
    llA.tail.next  tempNode
    llA.tail  tempNode
    llB.tail.next  tempNode
    llB.tail  tempNode

llA  LinkedList()
llA.generate(3,0, 10)

llB  LinkedList()
llB.generate(4,0, 10)

addSameNode(llA, llB, 11)
addSameNode(llA, llB, 14)

print(llA)
print(llB)

print(intersection(llA, llB))




    
