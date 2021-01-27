#   Created by Elshad Karimov on 02/06/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

# Use a single list to implement three stacks.

class MultiStack:
    ___ __init__(self, stacksize
        self.numberstacks = 3
        self.custList = [0] * (stacksize * self.numberstacks)
        self.sizes = [0] * self.numberstacks
        self.stacksize = stacksize
    
    ___ isFull(self, stacknum
        __ self.sizes[stacknum] == self.stacksize:
            r_ True
        ____
            r_ False
    
    ___ isEmpty(self, stacknum
        __ self.sizes[stacknum] == 0:
            r_ True
        ____
            r_ False
    
    ___ indexOfTop(self, stacknum
        offset = stacknum * self.stacksize
        r_ offset + self.sizes[stacknum]- 1
    
    ___ push(self, item, stacknum
        __ self.isFull(stacknum
            r_ "The stack is full"
        ____
            self.sizes[stacknum] += 1
            self.custList[self.indexOfTop(stacknum)] = item
    
    ___ pop(self, stacknum
        __ self.isEmpty(stacknum
            r_ "The stack is empty"
        ____
            value = self.custList[self.indexOfTop(stacknum)]
            self.custList[self.indexOfTop(stacknum)] = 0
            self.sizes[stacknum] -= 1
            r_ value
    
    ___ peek(self, stacknum
        __ self.isEmpty(stacknum
            r_ "The stack is empty"
        ____
            value = self.custList[self.indexOfTop(stacknum)]
            r_ value


customStack = MultiStack(6)
print(customStack.isFull(0))
print(customStack.isEmpty(1))
customStack.push(1, 0)
customStack.push(2, 0)
customStack.push(3, 2)
print(customStack.pop(0))
        
