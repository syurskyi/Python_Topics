c_ StackUnderflowError(E..
    p..


___ is_integer(s__
    ___
        i..(s__)
        r.. T..
    ______ V..
        r.. F..


___ evaluate(input_data
    __ n.. input_data:
        r.. []
    defines    # dict
    w.... input_data[0][:1] __ ':':
        values = input_data.pop(0).s.. 
        values.pop()
        values.pop(0)
        key = values.pop(0).l..
        __ is_integer(key
            r.. V...("Integers cannot be redefined")
        defines[key] = values
    stack    # list
    input_data = input_data[-1].s.. 
    w.... any(input_data
        word = input_data.pop(0).l..
        ___
            __ is_integer(word
                stack.a..(i..(word))
            ____ word __ defines:
                input_data = defines[word] + input_data
            ____ word __ '+':
                stack.a..(stack.pop() + stack.pop
            ____ word __ '-':
                stack.a..(-stack.pop() + stack.pop
            ____ word __ '*':
                stack.a..(stack.pop() * stack.pop
            ____ word __ '/':
                divisor = stack.pop()
                __ divisor __ 0:
                    r.. ZeroDivisionError("Attempted to divide by zero")
                stack.a..(i..(stack.pop() / divisor))
            ____ word __ 'dup':
                stack.a..(stack[-1])
            ____ word __ 'drop':
                stack.pop()
            ____ word __ 'swap':
                stack.a..(stack[-2])
                del stack[-3]
            ____ word __ 'over':
                stack.a..(stack[-2])
            ____:
                r.. V...("{} has not been defined".f..(word))
        ______ I..
            r.. StackUnderflowError("Insufficient number of items in stack")
    r.. stack
