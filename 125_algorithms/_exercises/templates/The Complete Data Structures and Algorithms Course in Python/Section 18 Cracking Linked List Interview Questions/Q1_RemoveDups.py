#   Created by Elshad Karimov on 17/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

# Question 1 - Remove Dups : Write a code to remove duplicates from an unsorted linked list. 


from LinkedList import LinkedList

___ removeDups(ll
    __ ll.head __ N..:
        r_
    ____
        currentNode = ll.head
        visited = set([currentNode.value])
        while currentNode.next:
            __ currentNode.next.value __ visited:
                currentNode.next = currentNode.next.next
            ____
                visited.add(currentNode.next.value)
                currentNode = currentNode.next
        r_ ll

___ removeDups1(ll
    __ ll.head __ N..:
        r_
    
    currentNode = ll.head
    while currentNode:
        runner = currentNode
        while runner.next:
            __ runner.next.value __ currentNode.value:
                runner.next = runner.next.next
            ____
                runner = runner.next
        currentNode = currentNode.next
    r_ ll.head



customLL = LinkedList()
customLL.generate(10, 0, 99)
print(customLL)
removeDups1(customLL)
print(customLL)