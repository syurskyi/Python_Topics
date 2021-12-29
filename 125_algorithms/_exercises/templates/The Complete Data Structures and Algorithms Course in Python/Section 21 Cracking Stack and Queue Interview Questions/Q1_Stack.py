#   Created by Elshad Karimov on 02/06/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

# Use a single list to implement three stacks.

c_ MultiStack:
    ___  -   stacksize
        numberstacks  3
        custList  [0] * (stacksize * numberstacks)
        sizes  [0] * numberstacks
        stacksize  stacksize
    
    ___ isFull  stacknum
        __ sizes[stacknum] __ stacksize:
            r_ T..
        ____
            r_ F..
    
    ___ isEmpty  stacknum
        __ sizes[stacknum] __ 0:
            r_ T..
        ____
            r_ F..
    
    ___ indexOfTop  stacknum
        offset  stacknum * stacksize
        r_ offset + sizes[stacknum]- 1
    
    ___ push  item, stacknum
        __ isFull(stacknum
            r_ "The stack is full"
        ____
            sizes[stacknum] + 1
            custList[indexOfTop(stacknum)]  item
    
    ___ pop  stacknum
        __ isEmpty(stacknum
            r_ "The stack is empty"
        ____
            value  custList[indexOfTop(stacknum)]
            custList[indexOfTop(stacknum)]  0
            sizes[stacknum] - 1
            r_ value
    
    ___ peek  stacknum
        __ isEmpty(stacknum
            r_ "The stack is empty"
        ____
            value  custList[indexOfTop(stacknum)]
            r_ value


customStack  MultiStack(6)
print(customStack.isFull(0))
print(customStack.isEmpty(1))
customStack.push(1, 0)
customStack.push(2, 0)
customStack.push(3, 2)
print(customStack.pop(0))
        
