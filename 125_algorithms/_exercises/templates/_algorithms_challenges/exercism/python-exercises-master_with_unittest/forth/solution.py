c_ StackUnderflowError(Exception):
    pass


___ is_integer(string):
    try:
        int(string)
        r.. T..
    except ValueError:
        r.. F..


___ evaluate(input_data):
    __ n.. input_data:
        r.. []
    defines    # dict
    w.... input_data[0][:1] __ ':':
        values = input_data.pop(0).s.. 
        values.pop()
        values.pop(0)
        key = values.pop(0).l..
        __ is_integer(key):
            raise ValueError("Integers cannot be redefined")
        defines[key] = values
    stack    # list
    input_data = input_data[-1].s.. 
    w.... any(input_data):
        word = input_data.pop(0).l..
        try:
            __ is_integer(word):
                stack.a..(int(word))
            ____ word __ defines:
                input_data = defines[word] + input_data
            ____ word __ '+':
                stack.a..(stack.pop() + stack.pop())
            ____ word __ '-':
                stack.a..(-stack.pop() + stack.pop())
            ____ word __ '*':
                stack.a..(stack.pop() * stack.pop())
            ____ word __ '/':
                divisor = stack.pop()
                __ divisor __ 0:
                    raise ZeroDivisionError("Attempted to divide by zero")
                stack.a..(int(stack.pop() / divisor))
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
                raise ValueError("{} has not been defined".f..(word))
        except IndexError:
            raise StackUnderflowError("Insufficient number of items in stack")
    r.. stack
