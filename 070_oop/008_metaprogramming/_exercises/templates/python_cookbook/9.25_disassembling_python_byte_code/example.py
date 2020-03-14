# Example of manual disassembly of bytecode

import opcode

def generate_opcodes(codebytes):
    extended_arg = 0
    i = 0
    n = len(codebytes)
    while i < n:
        op = codebytes[i]
        i += 1
        if op >= opcode.HAVE_ARGUMENT:
            oparg = codebytes[i] + codebytes[i+1]*256 + extended_arg
            extended_arg = 0
            i += 2
            if op == opcode.EXTENDED_ARG:
                extended_arg = oparg * 65536
                continue
        else:
            oparg = None
        yield (op, oparg)

# Example
def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
    print('Blastoff!')

for op, oparg in generate_opcodes(countdown.__code__.co_code):
    print(op, opcode.opname[op], oparg)

# Problem
# You want to know in detail what your code is doing under the covers by disassembling
# it into lower-level byte code used by the interpreter.
# Solution
# The dis module can be used to output a disassembly of any Python function. For
# example:

# Discussion
# The dis module can be useful if you ever need to study what’s happening in your program
# at a very low level (e.g., if you’re trying to understand performance characteristics).
# The raw byte code interpreted by the dis() function is available on functions as follows:

# If you ever want to interpret this code yourself, you would need to use some of the
# constants defined in the opcode module. For example:

# Ironically, there is no function in the dis module that makes it easy for you to process
# the byte code in a programmatic way. However, this generator function will take the raw
# byte code sequence and turn it into opcodes and arguments.

# Ironically, there is no function in the dis module that makes it easy for you to process
# the byte code in a programmatic way. However, this generator function will take the raw
# byte code sequence and turn it into opcodes and arguments.

# It’s a little-known fact, but you can replace the raw byte code of any function that you
# want. It takes a bit of work to do it, but here’s an example of what’s involved:

# Having the interpreter crash is a pretty likely outcome of pulling a crazy stunt like this.
# However, developers working on advanced optimization and metaprogramming tools
# might be inclined to rewrite byte code for real. This last part illustrates how to do it. See
# this code on ActiveState for another example of such code in action.