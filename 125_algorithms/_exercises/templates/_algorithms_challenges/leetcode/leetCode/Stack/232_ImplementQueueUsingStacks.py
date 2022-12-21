#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


c.. Queue o..
    """
    Use python list as the underlying data structure for stack.
    Add a "move()" method to simplify code: it moves all elements
    of the "inStack" to the "outStack" when the "outStack" is empty.
    """
    ___ __init__(self
        self.in_stack, self.out_stack   # list, []

    ___ push  x
        self.in_stack.append(x)

    ___ pop(self
        self.move()
        self.out_stack.pop()

    ___ peek(self
        self.move()
        r_ self.out_stack[-1]

    ___ empty(self
        r_ (n.. self.in_stack) and (n.. self.out_stack)

    ___ move(self
        __ n.. self.out_stack:
            _____ self.in_stack:
                self.out_stack.append(self.in_stack.pop())

'''
if __name__ == '__main__':
    q = Queue()
    q.push(2)
    q.push(3)
    q.push(4)
    print q.peek()
    q.pop()
    print q.peek()
    q.pop()
    q.pop()
    print q.empty()
'''
