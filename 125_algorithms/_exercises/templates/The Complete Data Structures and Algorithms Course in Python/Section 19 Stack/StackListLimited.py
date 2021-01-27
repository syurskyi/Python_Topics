#   Created by Elshad Karimov on 22/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

c_ Stack:
    ___  -   maxSize
        maxSize = maxSize
        list = []
    
    ___ __str__(self
        values = list.reverse()
        values = [str(x) ___ x __ list]
        r_ '\n'.join(values)
    
    # isEmpty
    ___ isEmpty(self
        __ list __ []:
            r_ T..
        ____
            r_ F..
    
    # isFull
    ___ isFull(self
        __ le_(list) __ maxSize:
            r_ T..
        ____
            r_ F..
    
    #  Push
    ___ push  value
        __ isFull(
            r_ "The stack is full"
        ____
            list.ap..(value)
            r_ "The element has been successfully inserted"
    # Pop
    ___ pop(self
        __ isEmpty(
            r_ "There is not any element in the stack"
        ____
            r_ list.pop()
    
    # peek
    ___ peek(self
        __ isEmpty(
            r_ "There is not any element in the stack"
        ____
            r_ list[le_(list)-1]

    #  delete
    ___ delete(self
        list = N..
    

customStack = Stack(4)
print(customStack.isEmpty())
print(customStack.isFull())
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack)

    