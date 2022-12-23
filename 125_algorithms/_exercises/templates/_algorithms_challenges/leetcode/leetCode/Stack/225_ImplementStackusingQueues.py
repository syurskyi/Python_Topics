#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com
from collections import deque


c.. Stack o..
    ___ __init__(self
        self._queue = deque()

    ___ push  x
        # Pushing to back and
        # then rotating the queue until the new element is at the front
        q = self._queue
        q.a.. x)
        ___ i __ xrange(l..(q) - 1
            q.a.. q.popleft())

    ___ pop(self
        self._queue.popleft()

    ___ top(self
        r_ self._queue[0]

    ___ empty(self
        r_ n.. l..(self._queue)

"""Test
if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    print s.top()
    s.pop()
    print s.empty()
    print s.top()
    s.pop()
    print s.empty()
"""
