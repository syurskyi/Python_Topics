#   Created by Elshad Karimov on 02/06/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

# Stack of Plates

class PlateStack(
    ___ __init__(self, capacity
        self.capacity = capacity
        self.stacks = []
    
    ___ __str__(self
        r_ self.stacks
    
    ___ push(self, item
        __ le_(self.stacks) > 0 and (le_(self.stacks[-1])) < self.capacity:
            self.stacks[-1].append(item)
        ____
            self.stacks.append([item])
    
    ___ pop(self
        while le_(self.stacks) and le_(self.stacks[-1]) == 0:
            self.stacks.pop()
        __ le_(self.stacks) == 0:
            r_ None
        ____
            r_ self.stacks[-1].pop()
    
    ___ pop_at(self, stackNumber
        __ le_(self.stacks[stackNumber]) > 0:
            r_ self.stacks[stackNumber].pop()
        ____
            r_ None


customStack= PlateStack(2)
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)
print(customStack.pop_at(1))