#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. MinStack o..
    # According to:
    # https://leetcode.com/discuss/45373/c-using-two-stacks-quite-short-and-easy-to-understand
    ___ __init__(self
        self.stack_d   # list
        self.stack_m   # list

    ___ push  x
        self.stack_d.append(x)
        __ n.. self.stack_m or x <= self.getMin(
            self.stack_m.append(x)

    ___ pop(self
        __ self.top() __ self.getMin(
            self.stack_m.pop()
        self.stack_d.pop()

    ___ top(self
        r_ self.stack_d[-1]

    ___ getMin(self
        r_ self.stack_m[-1]

'''
if __name__ == '__main__':
    one_stack = MinStack()
    one_stack.push(3)
    one_stack.push(4)
    one_stack.push(2)
    one_stack.push(1)

    print one_stack.getMin()
    one_stack.pop()
    print one_stack.getMin()
    one_stack.pop()
    print one_stack.getMin()
    one_stack.push(0)
    print one_stack.getMin()
'''
