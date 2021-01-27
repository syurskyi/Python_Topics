#   Created by Elshad Karimov on 19/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

class MultiStack:

    ___ __init__(self, stacksize
        self.numstacks = 3
        self.array = [0] * (stacksize * self.numstacks)
        self.sizes = [0] * self.numstacks
        self.stacksize = stacksize
        # print(self.array)
        # print(self.sizes)

    ___ Push(self, item, stacknum
        __ self.IsFull(stacknum
            raise Exception('Stack is full')
        self.sizes[stacknum] += 1
        self.array[self.IndexOfTop(stacknum)] = item

    ___ Pop(self, stacknum
        __ self.IsEmpty(stacknum
            raise Exception('Stack is empty')
        value = self.array[self.IndexOfTop(stacknum)]
        self.array[self.IndexOfTop(stacknum)] = 0
        self.sizes[stacknum] -= 1
        r_ value

    ___ Peek(self, stacknum
        __ self.IsEmpty(stacknum
            raise Exception('Stack is empty')
        r_ self.array[self.IndexOfTop(stacknum)]

    ___ IsEmpty(self, stacknum
        r_ self.sizes[stacknum] == 0

    ___ IsFull(self, stacknum
        r_ self.sizes[stacknum] == self.stacksize

    ___ IndexOfTop(self, stacknum
        offset = stacknum * self.stacksize
        r_ offset + self.sizes[stacknum] - 1

stack = MultiStack(1)

