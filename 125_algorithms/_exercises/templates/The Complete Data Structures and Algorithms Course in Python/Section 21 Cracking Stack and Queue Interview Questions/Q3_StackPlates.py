#   Created by Elshad Karimov on 02/06/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

# Stack of Plates

c_ PlateStack(
    ___  -   capacity
        capacity = capacity
        stacks = []
    
    ___ __str__(self
        r_ stacks
    
    ___ push  item
        __ le_(stacks) > 0 and (le_(stacks[-1])) < capacity:
            stacks[-1].ap..(item)
        ____
            stacks.ap..([item])
    
    ___ pop(self
        w__ le_(stacks) and le_(stacks[-1]) __ 0:
            stacks.pop()
        __ le_(stacks) __ 0:
            r_ N..
        ____
            r_ stacks[-1].pop()
    
    ___ pop_at  stackNumber
        __ le_(stacks[stackNumber]) > 0:
            r_ stacks[stackNumber].pop()
        ____
            r_ N..


customStack= PlateStack(2)
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)
print(customStack.pop_at(1))