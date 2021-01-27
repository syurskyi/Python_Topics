#   Created by Elshad Karimov on 22/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

class Stack:
    ___ __init__(self, maxSize
        self.maxSize = maxSize
        self.list = []
    
    ___ __str__(self
        values = self.list.reverse()
        values = [str(x) ___ x __ self.list]
        r_ '\n'.join(values)
    
    # isEmpty
    ___ isEmpty(self
        __ self.list == []:
            r_ True
        ____
            r_ False
    
    # isFull
    ___ isFull(self
        __ le_(self.list) == self.maxSize:
            r_ True
        ____
            r_ False
    
    #  Push
    ___ push(self, value
        __ self.isFull(
            r_ "The stack is full"
        ____
            self.list.append(value)
            r_ "The element has been successfully inserted"
    # Pop
    ___ pop(self
        __ self.isEmpty(
            r_ "There is not any element in the stack"
        ____
            r_ self.list.pop()
    
    # peek
    ___ peek(self
        __ self.isEmpty(
            r_ "There is not any element in the stack"
        ____
            r_ self.list[le_(self.list)-1]

    #  delete
    ___ delete(self
        self.list = None
    

customStack = Stack(4)
print(customStack.isEmpty())
print(customStack.isFull())
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack)

    