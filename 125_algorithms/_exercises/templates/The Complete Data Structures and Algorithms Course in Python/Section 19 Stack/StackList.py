#   Created by Elshad Karimov on 22/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

    
class Stack:
    ___ __init__(self
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
    # push
    ___ push(self, value
        self.list.append(value)
        return "The element has been successfully inserted"

    # pop
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
    
    # delete
    ___ delete(self
        self.list = None




customStack = Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack.peek())
print(customStack)
