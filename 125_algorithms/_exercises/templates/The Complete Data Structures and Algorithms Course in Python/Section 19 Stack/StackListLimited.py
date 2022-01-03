#   Created by Elshad Karimov on 22/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

c_ Stack:
    ___  -   maxSize
        maxSize  maxSize
        li__  []
    
    ___ __str__(self
        values  li__.__..
        values  [st.(x) ___ x __ li__]
        r_ '\n'.j..(values)
    
    # isEmpty
    ___ isEmpty(self
        __ li__ __ []:
            r_ T..
        ____
            r_ F..
    
    # isFull
    ___ isFull(self
        __ le_(li__) __ maxSize:
            r_ T..
        ____
            r_ F..
    
    #  Push
    ___ push  value
        __ isFull(
            r_ "The stack is full"
        ____
            li__.ap..(value)
            r_ "The element has been successfully inserted"
    # Pop
    ___ pop(self
        __ isEmpty(
            r_ "There is not any element in the stack"
        ____
            r_ li__.pop()
    
    # peek
    ___ peek(self
        __ isEmpty(
            r_ "There is not any element in the stack"
        ____
            r_ li__[le_(li__)-1]

    #  delete
    ___ delete(self
        li__  N..
    

customStack  Stack(4)
print(customStack.isEmpty())
print(customStack.isFull())
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack)

    