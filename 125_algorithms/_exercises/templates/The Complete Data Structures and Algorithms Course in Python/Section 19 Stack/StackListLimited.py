#   Created by Elshad Karimov on 22/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

class Stack:
    ___ __init__(self, maxSize
        self.maxSize = maxSize
        self.list = []
    
    ___ __str__(self
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)
    
    # isEmpty
    ___ isEmpty(self
        __ self.list == []:
            return True
        ____
            return False
    
    # isFull
    ___ isFull(self
        __ len(self.list) == self.maxSize:
            return True
        ____
            return False
    
    #  Push
    ___ push(self, value
        __ self.isFull(
            return "The stack is full"
        ____
            self.list.append(value)
            return "The element has been successfully inserted"
    # Pop
    ___ pop(self
        __ self.isEmpty(
            return "There is not any element in the stack"
        ____
            return self.list.pop()
    
    # peek
    ___ peek(self
        __ self.isEmpty(
            return "There is not any element in the stack"
        ____
            return self.list[len(self.list)-1]

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

    