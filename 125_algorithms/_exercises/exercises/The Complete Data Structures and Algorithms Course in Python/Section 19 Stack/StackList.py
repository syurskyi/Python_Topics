#   Created by Elshad Karimov on 22/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

    
c_ Stack:
    ___  - (self
        li__ = []
    
    ___ __str__(self
        values = li__.re..
        values = [st.(x) ___ x __ li__]
        r_ '\n'.j..(values)
    
    # isEmpty
    ___ isEmpty(self
        __ li__ __ []:
            r_ T..
        ____
            r_ F..
    # push
    ___ push  value
        li__.ap..(value)
        r_ "The element has been successfully inserted"

    # pop
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
    
    # delete
    ___ delete(self
        li__ = N..




customStack = Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack.peek())
print(customStack)
