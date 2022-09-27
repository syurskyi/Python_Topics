c_ Solution o..
    ___ validateStackSequences  pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        in_stack =    # list
        pos = 0
        w.. pos != l.. pushed):
            curr = pushed[pos]
            w.. l.. in_stack) > 0 and l.. popped) > 0 and in_stack[-1] __ popped[0]:
                in_stack.pop(-1)
                popped.pop(0)
            __ l.. popped) __ 0:
                break
            __ curr __ popped[0]:
                popped.pop(0)
            ____
                in_stack.append(curr)
            pos += 1
        w.. l.. in_stack) > 0 and l.. popped) > 0 and in_stack[-1] __ popped[0]:
            in_stack.pop(-1)
            popped.pop(0)
        __ l.. in_stack) __ 0:
            r_ T..
        r_ F..


__ ____ __ ____
    s  ?
    # print s.validateStackSequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1])
    # print s.validateStackSequences([2, 1, 0], [1, 2, 0])
    print s.validateStackSequences([1, 0, 3, 2], [0, 1, 2, 3])
