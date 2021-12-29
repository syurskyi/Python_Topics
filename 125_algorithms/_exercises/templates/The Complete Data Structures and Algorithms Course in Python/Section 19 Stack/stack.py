#   Created by Elshad Karimov on 19/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

c_ MultiStack:

    ___  -   stacksize
        numstacks  3
        array  [0] * (stacksize * numstacks)
        sizes  [0] * numstacks
        stacksize  stacksize
        # print(self.array)
        # print(self.sizes)

    ___ Push  item, stacknum
        __ IsFull(stacknum
            raise Exception('Stack is full')
        sizes[stacknum] + 1
        array[IndexOfTop(stacknum)]  item

    ___ Pop  stacknum
        __ IsEmpty(stacknum
            raise Exception('Stack is empty')
        value  array[IndexOfTop(stacknum)]
        array[IndexOfTop(stacknum)]  0
        sizes[stacknum] - 1
        r_ value

    ___ Peek  stacknum
        __ IsEmpty(stacknum
            raise Exception('Stack is empty')
        r_ array[IndexOfTop(stacknum)]

    ___ IsEmpty  stacknum
        r_ sizes[stacknum] __ 0

    ___ IsFull  stacknum
        r_ sizes[stacknum] __ stacksize

    ___ IndexOfTop  stacknum
        offset  stacknum * stacksize
        r_ offset + sizes[stacknum] - 1

stack  MultiStack(1)

