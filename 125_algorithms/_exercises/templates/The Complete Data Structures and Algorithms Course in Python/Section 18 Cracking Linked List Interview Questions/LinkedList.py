#   Created by Elshad Karimov on 17/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

____ random _____ randint
c_ Node:
    ___  -   valueN..
        value  value
        next  N..
        prev  N..
    
    ___ __str__(self
        r_ st.(value)

c_ LinkedList:
    ___  -   values  N..
        head  N..
        tail  N..

    ___ __iter__(self
        curNode  head
        w__ curNode:
            yield curNode
            curNode  curNode.next
    
    ___ __str__(self
        values  [st.(x.value) ___ x __ self]
        r_ ' -> '.j..(values)
    
    ___ __len__(self
        result  0
        node  head
        w__ node:
            result + 1
            node  node.next
        r_ result
    
    ___ add  value
        __ head __ N..:
            newNode  Node(value)
            head  newNode
            tail  newNode
        ____
            tail.next  Node(value)
            tail  tail.next
        r_ tail
    
    ___ generate  n, min_value, max_value
        head  N..
        tail  N..
        ___ i __ ra__(n
            add(randint(min_value,max_value))
        r_ self

# customLL = LinkedList()
# customLL.generate(10, 0, 99)
# print(customLL)
# print(len(customLL))

