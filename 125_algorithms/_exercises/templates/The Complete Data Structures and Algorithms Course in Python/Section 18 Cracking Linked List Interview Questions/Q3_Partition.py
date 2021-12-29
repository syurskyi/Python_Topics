#   Created by Elshad Karimov on 18/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

#  Question 3 - Write code to partition a linked list around a value x, 
#               such that all nodes less than x come before all nodes greater than or equal to x. 

____ LinkedList _____ LinkedList

___ partition(ll, x
    curNode  ll.head
    ll.tail  ll.head

    w__ curNode:
        nextNode  curNode.next
        curNode.next  N..
        __ curNode.value < x:
            curNode.next  ll.head
            ll.head  curNode
        ____
            ll.tail.next  curNode
            ll.tail  curNode
        curNode  nextNode
    
    __ ll.tail.next __ no. N..:
        ll.tail.next  N..

customLL  LinkedList()
customLL.generate(10,0,99)
print(customLL)
partition(customLL, 30)
print(customLL)