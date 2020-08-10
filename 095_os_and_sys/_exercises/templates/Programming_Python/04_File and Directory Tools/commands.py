#!/usr/local/bin/python
____ ___ ______ a..
____ scanfile ______ scanner
class UnknownCommand(Exception): pass

___ processLine(line):                      # define a function
    __ line[0] __ '*':                      # applied to each line
        print("Ms.", line[1:-1])
    ____ line[0] __ '+':
        print("Mr.", line[1:-1])            # strip first and last char: \n
    ____
        raise UnknownCommand(line)          # raise an exception

filename _ 'data.txt'
__ le.(a..) __ 2: filename _ a..[1]       # allow filename cmd arg
scanner(filename, processLine)              # start the scanner


"""
commands = {'*': 'Ms.', '+': 'Mr.'}     # data is easier to expand than code?

def processLine(line):
    ___
        print(commands[line[0]], line[1:-1])
    ______ KeyError:
        raise UnknownCommand(line)

scanner(argv[1], processLine)
"""